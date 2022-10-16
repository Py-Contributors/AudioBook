import os
from tqdm import tqdm
import PyPDF2
import pyttsx3
import ebooklib
from ebooklib import epub

import logging
logger = logging.getLogger("PyPDF2")
logger.setLevel(logging.INFO)

from audiobook.utils import response_to_text
from audiobook.utils import speak_text
from audiobook.utils import text_preprocessing
from audiobook.utils import load_json
from audiobook.utils import write_json_file

from audiobook.article_web_scraper import ArticleWebScraper

from audiobook.config import speed_dict
from audiobook.config import supported_file_types


expand_usr = os.path.expanduser("~")
BOOK_DIR = os.path.join(expand_usr, "audiobook/library")
os.makedirs(BOOK_DIR, exist_ok=True)

logger = logging.getLogger("PyPDF2")
logger.setLevel(logging.INFO)

class AudioBook:
    """
    AudioBook class

    methods:
        file_check: checks if file exists
        pdf_to_json: converts pdf to json format
        create_json_book: Creates json book from input file by calling respective method
        read_json: reads a json file
        save_json_to_audio: save .mp3 audios from a json file in a folder
        save_book_audio: saves audio files in folder
        read_book: reads the book
        read_web_article: read web article from a given url
        save_web_article_audio: save web article to a .mp3 file from a given url
    sample usage:
        ab = AudioBook(speed="normal")
        ab.read_book(file_path, password="abcd")
    """

    def __init__(self, speed="normal", volume=1.0):
        self.engine = pyttsx3.init()
        self.engine.setProperty("rate", speed_dict[speed])
        self.engine.setProperty("volume", volume)
        # set escape key to stop pyttsx3

    # get all books in library
    def get_library(self):
        """ get all books in library """
        total_books = os.listdir(BOOK_DIR)
        if len(total_books) == 0:
            return "You have no books in your library"
        print("You Have total {} books in your library".format(len(total_books)))
        return total_books

    def file_check(self, input_file_path):
        """ checks file format and if file exists """
        if not os.path.exists(input_file_path):
            raise FileNotFoundError("File not found!")

        if not input_file_path.endswith(supported_file_types):
            raise IsADirectoryError("File format not supported!")

    def pdf_to_json(self, input_file_path, password=None):
        """ sub method to create json book from pdf file"""
        json_book = {}
        with open(input_file_path, "rb") as fp:
            pdfReader = PyPDF2.PdfFileReader(fp)
            if pdfReader.isEncrypted:
                logging.info("File is encrypted, trying to decrypt...")
                pdfReader.decrypt(password)
            pages = pdfReader.numPages
            for page_num in range(0, pages):
                pageObj = pdfReader.getPage(page_num)
                extracted_text = pageObj.extractText()
                json_book[str(page_num)] = extracted_text
        return json_book, pages

    def txt_to_json(self, input_file_path):
        """ sub method to create json book from txt file """
        json_book = {}
        with open(input_file_path, "r") as fp:
            file_txt_data = fp.read()
        for i in range(0, len(file_txt_data), 2000):
            page_num = i // 2000
            json_book[str(page_num)] = file_txt_data[i:i + 2000]
        return json_book, len(json_book)

    def mobi_to_json(self, input_file_path):
        """ sub method to create json book from mobi file """
        pass

    def docs_to_json(self, input_file_path):
        """ sub method to create json book from docs file """
        pass

    def epub_to_json(self, input_file_path):
        json_book = {}
        book = epub.read_epub(input_file_path)
        text = " ".join([response_to_text(chapter.get_body_content()) for chapter in book.get_items_of_type(ebooklib.ITEM_DOCUMENT)])
        for i in range(1, len(text) + 1, 2000):
            page_num = i // 2000
            json_book[str(page_num)] = text[i:i + 2000]

        return json_book, len(json_book)

    def create_json_book(self, input_file_path, password=None):
        """ method to create json book from input file
            it calls respective method based on file format """
        self.file_check(input_file_path)
        filename = os.path.basename(input_file_path).split(".")[0] + ".json"

        if input_file_path.endswith(".pdf"):
            json_book, pages = self.pdf_to_json(input_file_path, password)
        elif input_file_path.endswith(".txt"):
            json_book, pages = self.txt_to_json(input_file_path)
        elif input_file_path.endswith(".epub"):
            json_book, pages = self.epub_to_json(input_file_path)

        write_json_file(json_book, os.path.join(BOOK_DIR, filename))

        return json_book, pages

   def save_audio(self, input_file_path, password=None):
        """ method to save audio files in folder """
        self.file_check(input_file_path)

        json_filename = os.path.basename(input_file_path).split(".")[0] + ".json"
        book_name = os.path.basename(input_file_path).split(".")[0]

        # if json book already exists, load it from library
        if os.path.exists(os.path.join(BOOK_DIR, json_filename)):
            print("Book already exists in library")
            logging.info("Loading json book from {}".format(json_filename))
            json_book = load_json(os.path.join(BOOK_DIR, json_filename))
            pages = len(json_book)
        else:
            print("Creating your audiobook... Please wait...")
            json_book, pages = self.create_json_book(input_file_path, password)

        os.makedirs(book_name, exist_ok=True)
        print('Saving audio files in folder: {}'.format(book_name))
        for page_num, text in tqdm(json_book.items()):
            self.engine.save_to_file(text, os.path.join(book_name, book_name + "_page_" + (str(page_num)) + ".mp3"))
            self.engine.runAndWait()
    
    def read_book(self, input_file_path, password=None):  # argument to be added, save_audio=False, save_json_book=False
        """ method to read the book """
        self.file_check(input_file_path)
        json_filename = os.path.basename(input_file_path).split(".")[0] + ".json"

        # if json book already exists, load it from library
        if os.path.exists(os.path.join(BOOK_DIR, json_filename)):
            logging.info("Loading json book from {}".format(json_filename))
            json_book = load_json(os.path.join(BOOK_DIR, json_filename))
            pages = len(json_book)
        else:
            print("Creating your audiobook... Please wait...")
            json_book, pages = self.create_json_book(input_file_path, password)

        speak_text(self.engine, f"The book has total {str(pages)} pages!")
        speak_text(self.engine, "Please enter the page number: ", display=False)
        start_page = int(input("Please enter the page number: ")) - 1

        reading = True
        while reading:
            if start_page > pages or start_page < 0:
                speak_text(self.engine, "Invalid page number!")
                speak_text(self.engine, f"The book has total {str(pages)} pages!")
                start_page = int(input("Please enter the page number: "))

            speak_text(self.engine, f"Reading page {str(start_page+1)}")
            pageText = json_book[str(start_page)]
            speak_text(self.engine, pageText, display=False)

            user_input = input("Please Select an option: \n 1. Type 'r' to read again: \n 2. Type 'p' to read previous page\n 3. Type 'n' to read next page\n 4. Type 'q' to quit:\n 5. Type page number to read that page:\n")
            if user_input == "r":
                speak_text(self.engine, f"Reading page {str(start_page+1)}")
                continue
            elif user_input == "p":
                speak_text(self.engine, "Reading previous page")
                start_page -= 1
                continue
            elif user_input == "n":
                speak_text(self.engine, "Reading next page")
                start_page += 1
                continue
            elif user_input == "q":
                speak_text(self.engine, "Quitting the book!")
                break
            elif user_input.isnumeric():
                start_page = int(user_input) - 1
            else:
                user_input = input("Please Select an option: \n 1. Type 'r' to read again: \n 2. Type 'p' to read previous page\n 3. Type 'n' to read next page\n 4. Type 'q' to quit:\n 5. Type page number to read that page:\n")
                continue


    def save_json_to_audio(self, json, audio_name):
        """ save json to a list of file in a folder having audio_name, one for each page """
        os.makedirs(audio_name, exist_ok=True)
        logger.info('Saving audio files in folder: {}'.format(audio_name))
        for page_num, text in json.items():
            self.engine.save_to_file(text, os.path.join(audio_name, audio_name + "_page_" + (str(page_num+1) + ".mp3")))
            self.engine.runAndWait()

    def read_web_article(self, article_url):
        """ read web article from a article_url containing an <article> tag """
        ws = ArticleWebScraper(article_url)
        json_article, pages = ws.get_json_from_web_article()
        if len(json_article) > 0:
            self.read_json(json_article, pages, "article")
        else:
            raise ValueError("<article> tag has no text.")
    
    def save_web_article_audio(self, article_url):
        """ save web article from a article_url containing an <article> tag """
        ws = ArticleWebScraper(article_url)
        json_article, _ = ws.get_json_from_web_article()
        if len(json_article) > 0:
            title = ws.get_title_from_article()
            folder_name = input(f"Choose name for article \"{title}\". It will be stored in {os.getcwd()}\n")
            self.save_json_to_audio(json_article, folder_name)
        else:
            raise ValueError("<article> tag is empty.")
        

        
