from bs4 import BeautifulSoup
import re
import json
import PyPDF2
import ebooklib
from ebooklib import epub

regex = re.compile(r'[\n\r\t]')

from audiobook.article_web_scraper import ArticleWebScraper

def load_json(filename):
    with open(filename, "r") as fp:
        return json.load(fp)


def write_json_file(json_data, filename):
    with open(filename, "w") as fp:
        json.dump(json_data, fp)


def text_preprocessing(input_text):
    preprocessed_text = [regex.sub("", t) for t in input_text]
    preprocessed_text = [re.sub(' +', ' ', t) for t in preprocessed_text]
    return preprocessed_text

def pdf_to_json(self, input_book_path, password=None):
    """ sub method to create json book from pdf file"""
    json_book = {}
    with open(input_book_path, "rb") as fp:
        pdfReader = PyPDF2.PdfFileReader(fp)
        if pdfReader.isEncrypted:
            pdfReader.decrypt(password)
        pages = pdfReader.numPages
        for page_num in range(0, pages):
            pageObj = pdfReader.getPage(page_num)
            extracted_text = pageObj.extractText()
            json_book[str(page_num)] = extracted_text
    return json_book, pages

def txt_to_json(self, input_book_path):
    """ sub method to create json book from txt file """
    json_book = {}
    with open(input_book_path, "r") as fp:
        file_txt_data = fp.read()
    for i in range(0, len(file_txt_data), 2000):
        page_num = i // 2000
        json_book[str(page_num)] = file_txt_data[i:i + 2000]
    return json_book, len(json_book)     

def mobi_to_json(self, input_book_path):
    """ sub method to create json book from mobi file """
    pass

def docs_to_json(self, input_book_path):
    """ sub method to create json book from docs file """
    pass

def epub_to_json(self, input_book_path):
    json_book = {}
    book = epub.read_epub(input_book_path)
    text = " ".join([response_to_text(chapter.get_body_content()) for chapter in book.get_items_of_type(ebooklib.ITEM_DOCUMENT)])
    for i in range(1, len(text) + 1, 2000):
        page_num = i // 2000
        json_book[str(page_num)] = text[i:i + 2000]

    return json_book, len(json_book)

def html_to_json(self, url):
    """ method to create json book from web article """
    json_book = {}
    article_scraper = ArticleWebScraper(url)
    page_data = article_scraper.get_page_data()
    for i in range(0, len(page_data), 2000):
        page_num = i // 2000
        json_book[str(page_num)] = page_data[i:i + 2000]

    return json_book, len(json_book)   
    
def response_to_text(chapter):
    """ fuction to convert response to text

        required for epub files
        maybe required for html files
    """
    soup = BeautifulSoup(chapter, 'html.parser')
    extracted_text = [para.get_text() for para in soup.find_all('p')]
    preprocessed_text = text_preprocessing(extracted_text)
    # remove unicode characters
    return ' '.join(preprocessed_text)


def speak_text(engine, text, display=True):
    """ function to speak text and display it """
    if display:
        print(text)
    engine.say(text)
    engine.runAndWait()


# def file_check(self, input_book_path):
#     """ checks file format and if file exists """
#     if not os.path.exists(input_book_path):
#         raise FileNotFoundError("File not found!")

#     if not input_book_path.endswith(supported_file_types):
#         raise IsADirectoryError("File format not supported!")