import json
import os
import re

import docx2txt
import ebooklib
import html2text
import mobi
from bs4 import BeautifulSoup
from ebooklib import epub
from odf import text, teletype
from odf.opendocument import load

from audiobook.doc_parser.web_parser import ArticleWebScraper
from audiobook.doc_parser.pdf_parser import PyPDF2DocParser
from audiobook.doc_parser.pdf_parser import PdfMinerDocParser


def load_json(filename):
    with open(filename, "r") as fp:
        return json.load(fp)


def write_json_file(json_data, filename):
    with open(filename, "w") as fp:
        json.dump(json_data, fp)


def text_preprocessing(input_text):
    """function to preprocess text"""
    regex = re.compile(r"[\n\r\t]")
    preprocessed_text = regex.sub("", input_text)
    preprocessed_text = re.sub(" +", " ", preprocessed_text)
    preprocessed_text = preprocessed_text.strip()
    return preprocessed_text


def response_to_text(chapter):
    """fuction to convert response to text

    required for epub files
    maybe required for html files
    """
    soup = BeautifulSoup(chapter, "html.parser")
    extracted_text = [para.get_text() for para in soup.find_all("p")]
    extracted_text = " ".join(extracted_text)
    preprocessed_text = text_preprocessing(extracted_text)
    return preprocessed_text


def speak_text(engine, text, display=True):
    """function to speak text and display it"""
    if display:
        print(text)
    engine.say(text)
    engine.runAndWait()


def mobi_to_json(input_book_path):
    """sub method to create json book from mobi file"""
    metadata = {}
    json_book = {}
    book_name = os.path.basename(input_book_path).split(".")[0]
    tempdir, filepath = mobi.extract(input_book_path)
    with open(filepath, "r", encoding="utf-8") as fp:
        content = fp.read()
    book_data = html2text.html2text(content)
    book_data = text_preprocessing(book_data)

    for i in range(0, len(book_data), 2000):
        page_num = i // 2000
        json_book[str(page_num)] = book_data[i: i + 2000]

    metadata["pages"] = len(json_book)
    metadata["book_name"] = book_name
    return json_book, metadata


def pdf_to_json(input_book_path, password=None, extraction_engine="pypdf2"):
    """sub method to create json book from pdf file"""
    metadata = {}
    json_book = {}
    basename = os.path.basename(input_book_path).split(".")[0]
    if extraction_engine is None or extraction_engine == "pdfminer":
        print("Using pdfminer")
        pdf_parser = PdfMinerDocParser()
    elif extraction_engine == "pypdf2":
        print("Using pypdf2")
        pdf_parser = PyPDF2DocParser()
    else:
        raise NotImplementedError("Only pdfminer and pypdf2 are supported")

    text = pdf_parser.get_text(input_book_path, password=password)
    text = text_preprocessing(text)

    for i in range(0, len(text), 2000):
        page_num = i // 2000
        json_book[str(page_num)] = text[i: i + 2000]

    metadata['book_name'] = basename
    metadata['pages'] = len(json_book)
    return json_book, metadata


def odt_to_json(input_book_path):
    """sub method to create json book from odt file"""
    metadata = {}
    json_book = {}
    basename = os.path.basename(input_book_path).split(".")[0]

    textdoc = load(input_book_path)
    allparas = textdoc.getElementsByType(text.P)
    output_text = ""
    for i in range(len(allparas)):
        output_text += " " + teletype.extractText(allparas[i])
    output_text = text_preprocessing(output_text)

    for i in range(0, len(output_text), 2000):
        page_num = i // 2000
        json_book[str(page_num)] = output_text[i: i + 2000]

    metadata['book_name'] = basename
    metadata['pages'] = len(json_book)

    return json_book, metadata


def txt_to_json(input_book_path):
    """sub method to create json book from txt file"""
    json_book = {}
    metadata = {}
    book_name = os.path.basename(input_book_path).split(".")[0]
    with open(input_book_path, "r") as fp:
        file_txt_data = fp.read()
    file_txt_data = text_preprocessing(file_txt_data)

    for i in range(0, len(file_txt_data), 2000):
        page_num = i // 2000
        json_book[str(page_num)] = file_txt_data[i: i + 2000]

    metadata["pages"] = len(json_book)
    metadata["book_name"] = book_name
    return json_book, metadata


def docs_to_json(input_book_path):
    """sub method to create json book from docs file"""
    metadata = {}
    json_book = {}
    book_name = os.path.basename(input_book_path).split(".")[0]
    book_data = docx2txt.process(input_book_path)
    for i in range(0, len(book_data), 2000):
        page_num = i // 2000
        json_book[str(page_num)] = book_data[i: i + 2000]

    metadata["pages"] = len(json_book)
    metadata["book_name"] = book_name
    return json_book, metadata


def epub_to_json(input_book_path):
    metadata = {}
    json_book = {}
    book_name = os.path.basename(input_book_path).split(".")[0]
    book = epub.read_epub(input_book_path)
    text = " ".join(
        [
            response_to_text(chapter.get_body_content())
            for chapter in book.get_items_of_type(ebooklib.ITEM_DOCUMENT)
        ]
    )
    for i in range(1, len(text) + 1, 2000):
        page_num = i // 2000
        json_book[str(page_num)] = text[i: i + 2000]

    metadata["pages"] = len(json_book)
    metadata["book_name"] = book_name
    return json_book, metadata


def html_to_json(url):
    """method to create json book from web article"""
    metadata = {}
    json_book = {}
    book_name = os.path.basename(url).split(".")[0]
    article_scraper = ArticleWebScraper(url)
    page_data = article_scraper.get_page_data()
    page_data = text_preprocessing(page_data)
    for i in range(0, len(page_data), 2000):
        page_num = i // 2000
        json_book[str(page_num)] = page_data[i: i + 2000]

    metadata["pages"] = len(json_book)
    metadata["book_name"] = book_name
    return json_book, metadata
