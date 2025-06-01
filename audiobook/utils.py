import json
import os
import re
import docx2txt
import ebooklib
from bs4 import BeautifulSoup
from ebooklib import epub
from odf import text, teletype
from odf.opendocument import load
from striprtf.striprtf import rtf_to_text
from audiobook.doc_parser.web_parser import ArticleWebScraper
from audiobook.doc_parser.pdf_parser import PyPDF2DocParser

# Helper function to load JSON data from a file
def load_json(filename):
    with open(filename, "r") as fp:
        return json.load(fp)

# Helper function to write JSON data to a file
def write_json_file(json_data, filename):
    with open(filename, "w") as fp:
        json.dump(json_data, fp)

# Text preprocessing: removes unwanted characters and extra spaces
def text_preprocessing(input_text):
    preprocessed_text = re.sub(r"[\n\r\t]", "", input_text)
    preprocessed_text = re.sub(" +", " ", preprocessed_text).strip()
    return preprocessed_text

# Extract text content from HTML, preprocess it
def response_to_text(chapter):
    soup = BeautifulSoup(chapter, "html.parser")
    extracted_text = " ".join([para.get_text() for para in soup.find_all("p")])
    return text_preprocessing(extracted_text)

# Speak the given text using the engine
def speak_text(engine, text, display=True):
    if display:
        print(text)
    engine.say(text)
    engine.runAndWait()


# Helper function to convert PDF to JSON format
def pdf_to_json(input_book_path, password=None):
    json_book = {}
    metadata = {}
    basename = os.path.basename(input_book_path).split(".")[0]

    pdf_parser = PyPDF2DocParser()
    text = pdf_parser.get_text(input_book_path, password=password)
    text = text_preprocessing(text)

    json_book = {str(i // 2000): text[i:i + 2000] for i in range(0, len(text), 2000)}
    
    metadata["book_name"] = basename
    metadata["pages"] = len(json_book)
    return json_book, metadata

# Helper function to convert ODT files to JSON format
def odt_to_json(input_book_path):
    json_book = {}
    metadata = {}
    basename = os.path.basename(input_book_path).split(".")[0]

    textdoc = load(input_book_path)
    output_text = " ".join([teletype.extractText(para) for para in textdoc.getElementsByType(text.P)])
    output_text = text_preprocessing(output_text)

    json_book = {str(i // 2000): output_text[i:i + 2000] for i in range(0, len(output_text), 2000)}
    
    metadata["book_name"] = basename
    metadata["pages"] = len(json_book)
    return json_book, metadata

# Helper function to convert TXT files to JSON format
def txt_to_json(input_book_path):
    json_book = {}
    metadata = {}
    book_name = os.path.basename(input_book_path).split(".")[0]
    
    with open(input_book_path, "r") as fp:
        file_txt_data = fp.read()
    
    file_txt_data = text_preprocessing(file_txt_data)
    json_book = {str(i // 2000): file_txt_data[i:i + 2000] for i in range(0, len(file_txt_data), 2000)}
    
    metadata["pages"] = len(json_book)
    metadata["book_name"] = book_name
    return json_book, metadata

# Helper function to convert RTF files to JSON format
def rtf_to_json(input_book_path):
    json_book = {}
    metadata = {}
    book_name = os.path.basename(input_book_path).split(".")[0]

    with open(input_book_path, "r") as fp:
        file_rtf_data = fp.read()
    
    file_txt_data = rtf_to_text(file_rtf_data, errors="ignore")
    file_txt_data = text_preprocessing(file_txt_data)

    json_book = {str(i // 2000): file_txt_data[i:i + 2000] for i in range(0, len(file_txt_data), 2000)}
    
    metadata["pages"] = len(json_book)
    metadata["book_name"] = book_name
    return json_book, metadata

# Helper function to convert DOCX files to JSON format
def docs_to_json(input_book_path):
    json_book = {}
    metadata = {}
    book_name = os.path.basename(input_book_path).split(".")[0]
    
    book_data = docx2txt.process(input_book_path)
    json_book = {str(i // 2000): book_data[i:i + 2000] for i in range(0, len(book_data), 2000)}
    
    metadata["pages"] = len(json_book)
    metadata["book_name"] = book_name
    return json_book, metadata

# Helper function to convert EPUB files to JSON format
def epub_to_json(input_book_path):
    json_book = {}
    metadata = {}
    book_name = os.path.basename(input_book_path).split(".")[0]
    
    book = epub.read_epub(input_book_path)
    text = " ".join([response_to_text(chapter.get_body_content()) for chapter in book.get_items_of_type(ebooklib.ITEM_DOCUMENT)])
    
    json_book = {str(i // 2000): text[i:i + 2000] for i in range(1, len(text) + 1, 2000)}
    
    metadata["pages"] = len(json_book)
    metadata["book_name"] = book_name
    return json_book, metadata

# Helper function to convert HTML (web) content to JSON format
def html_to_json(url):
    metadata = {}
    json_book = {}
    book_name = os.path.basename(url).split(".")[0]
    
    article_scraper = ArticleWebScraper(url)
    page_data = article_scraper.get_page_data()
    page_data = text_preprocessing(page_data)
    
    json_book = {str(i // 2000): page_data[i:i + 2000] for i in range(0, len(page_data), 2000)}
    
    metadata["pages"] = len(json_book)
    metadata["book_name"] = book_name
    return json_book, metadata

# Main function to determine the file type and call respective methods
def get_json_metadata(input_book_path, password=None):
    file_extension = input_book_path.split(".")[-1].lower()
    json_book, metadata = {}, {}

    file_to_json = {
        "odt": odt_to_json,
        "pdf": pdf_to_json,
        "txt": txt_to_json,
        "epub": epub_to_json,
        "html": html_to_json,
        "docx": docs_to_json,
        "rtf": rtf_to_json
    }

    if file_extension in file_to_json:
        json_book, metadata = file_to_json[file_extension](input_book_path)
    else:
        raise NotImplementedError(f"Unsupported file type: {file_extension}")
    
    return json_book, metadata
