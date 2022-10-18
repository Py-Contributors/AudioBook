from bs4 import BeautifulSoup
import re
import os
import json
import PyPDF2
import ebooklib
from ebooklib import epub
import mobi

import html2text
regex = re.compile(r'[\n\r\t]')

from audiobook.article_web_scraper import ArticleWebScraper

def load_json(filename):
    with open(filename, "r") as fp:
        return json.load(fp)

def write_json_file(json_data, filename):
    with open(filename, "w") as fp:
        json.dump(json_data, fp)

def text_preprocessing(input_text):
    """ function to preprocess text """
    preprocessed_text = regex.sub("", input_text) 
    preprocessed_text = re.sub(' +', ' ', preprocessed_text)
    return preprocessed_text
          
def response_to_text(chapter):
    """ fuction to convert response to text

        required for epub files
        maybe required for html files
    """
    soup = BeautifulSoup(chapter, 'html.parser')
    extracted_text = [para.get_text() for para in soup.find_all('p')]
    extracted_text = ' '.join(extracted_text)
    preprocessed_text = text_preprocessing(extracted_text)
    return preprocessed_text               

def speak_text(engine, text, display=True):
    """ function to speak text and display it """
    if display:
        print(text)
    engine.say(text)
    engine.runAndWait()

def mobi_to_json(input_book_path):
    """ sub method to create json book from mobi file """
    metadata = {}
    json_book = {}
    book_name = os.path.basename(input_book_path).split(".")[0]
    tempdir, filepath = mobi.extract(input_book_path)
    with open(filepath, "r", encoding='utf-8') as fp:
        content = fp.read()
    book_data = html2text.html2text(content)
    book_data = text_preprocessing(book_data)
    
    for i in range(0, len(book_data), 2000):
        page_num = i // 2000
        json_book[str(page_num)] = book_data[i:i + 2000]

    metadata["pages"] = len(json_book)
    metadata["book_name"] = book_name
    return json_book, metadata

def pdf_to_json(input_book_path, password=None):
    """ sub method to create json book from pdf file"""
    metadata = {}
    json_book = {}
    book_name = os.path.basename(input_book_path).split(".")[0]
    with open(input_book_path, "rb") as fp:
        pdfReader = PyPDF2.PdfFileReader(fp)
        if pdfReader.isEncrypted:
            pdfReader.decrypt(password)
            
        information = pdfReader.getDocumentInfo()

        metadata["author"] = information.author
        metadata["creator"] = information.creator
        metadata["producer"] = information.producer
        metadata["subject"] = information.subject
        metadata["title"] = information.title
        metadata["pages"] = pdfReader.numPages
        metadata["book_name"] = book_name
        
        pages = pdfReader.numPages
        for page_num in range(0, pages):
            pageObj = pdfReader.getPage(page_num)
            extracted_text = pageObj.extractText()
            json_book[str(page_num)] = extracted_text

    return json_book, metadata

def txt_to_json(input_book_path):
    """ sub method to create json book from txt file """
    json_book = {}
    metadata = {}
    book_name = os.path.basename(input_book_path).split(".")[0]
    with open(input_book_path, "r") as fp:
        file_txt_data = fp.read()
    file_txt_data = text_preprocessing(file_txt_data)
    
    for i in range(0, len(file_txt_data), 2000):
        page_num = i // 2000
        json_book[str(page_num)] = file_txt_data[i:i + 2000]
    
    metadata["pages"] = len(json_book)
    metadata["book_name"] = book_name
    return json_book, metadata   


def docs_to_json(input_book_path):
    """ sub method to create json book from docs file """
    pass

def epub_to_json(input_book_path):
    metadata = {}
    json_book = {}
    book_name = os.path.basename(input_book_path).split(".")[0]
    book = epub.read_epub(input_book_path)
    text = " ".join([response_to_text(chapter.get_body_content()) for chapter in book.get_items_of_type(ebooklib.ITEM_DOCUMENT)])
    for i in range(1, len(text) + 1, 2000):
        page_num = i // 2000
        json_book[str(page_num)] = text[i:i + 2000]
    
    metadata["pages"] = len(json_book)
    metadata["book_name"] = book_name
    return json_book, metadata

def html_to_json(url):
    """ method to create json book from web article """
    metadata = {}
    json_book = {}
    book_name = os.path.basename(url).split(".")[0]
    article_scraper = ArticleWebScraper(url)
    page_data = article_scraper.get_page_data()
    page_data = text_preprocessing(page_data)
    for i in range(0, len(page_data), 2000):
        page_num = i // 2000
        json_book[str(page_num)] = page_data[i:i + 2000]

    metadata["pages"] = len(json_book)
    metadata["book_name"] = book_name
    return json_book, metadata
    

