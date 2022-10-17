
import os
from re import I
from tqdm import tqdm
import pyttsx3
import logging
logger = logging.getLogger("PyPDF2")
logger.setLevel(logging.INFO)

from audiobook.utils import response_to_text
from audiobook.utils import speak_text
from audiobook.utils import text_preprocessing
from audiobook.utils import load_json
from audiobook.utils import write_json_file

from audiobook.utils import pdf_to_json
from audiobook.utils import txt_to_json
from audiobook.utils import mobi_to_json
from audiobook.utils import docs_to_json
from audiobook.utils import epub_to_json
from audiobook.utils import html_to_json


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
        web_page_to_json: converts web article to json
        create_json_book: Creates json book from input file by calling respective method
        read_json: reads a json file
        save_json_to_audio: save .mp3 audios from a json file in a folder
        save_book_audio: saves audio files in folder
        read_book: reads the book
        
    sample usage:
        ab = AudioBook(speed="normal")
        ab.read_book(file_path, password="abcd")
    """

    def __init__(self, speed="normal", volume=1.0):
        self.engine = pyttsx3.init()
        self.engine.setProperty("rate", speed_dict[speed])
        self.engine.setProperty("volume", volume)

    def get_library(self):
        """ get all books in library """
        total_books = os.listdir(BOOK_DIR)
        if len(total_books) == 0:
            return "You have no books in your library"
        print("You Have total {} books in your library".format(len(total_books)))
        return total_books
    
    def create_json_book(self, input_book_path, password=None):
        """ method to create json book from input file
            it calls respective method based on file format """
        json_filename = os.path.basename(input_book_path).split(".")[0] + ".json"
        
        if os.path.exists(os.path.join(BOOK_DIR, json_filename)):
            print("Book already exists in library, reading from library")
            json_book = load_json(os.path.join(BOOK_DIR, json_filename))
            pages = len(json_book)
            return json_book, pages
        
        elif input_book_path.endswith(".pdf"):
            json_book, pages = pdf_to_json(input_book_path, password)
        elif input_book_path.endswith(".txt"):
            json_book, pages = txt_to_json(input_book_path)
        elif input_book_path.endswith(".epub"):
            json_book, pages = epub_to_json(input_book_path)
        elif input_book_path.endswith(".mobi"):
            json_book, pages = mobi_to_json(input_book_path)
        elif input_book_path.startswith("http"):
            json_book, pages = html_to_json(input_book_path)
        
        write_json_file(json_book, os.path.join(BOOK_DIR, json_filename))

        return json_book, pages

    def save_audio(self, input_book_path, password=None, save_page_wise=False):
        """ method to save audio files in folder """
        json_book, _ = self.create_json_book(input_book_path, password)
        
        book_name = os.path.basename(input_book_path).split(".")[0]
        os.makedirs(book_name, exist_ok=True)
        
        print('Saving audio files in folder: {}'.format(book_name))
        
        if save_page_wise:
            for page_num, text in tqdm(json_book.items()):
                self.engine.save_to_file(text, os.path.join(book_name, 
                                                            book_name + 
                                                            "_page_" + 
                                                            (str(page_num)) + 
                                                            ".mp3"))
                self.engine.runAndWait()

        elif not save_page_wise:
            all_text = " ".join([text for text in json_book.values()])
            self.engine.save_to_file(all_text, os.path.join(book_name, book_name + ".mp3"))
            self.engine.runAndWait()
            
    def read_book(self, input_book_path, password=None):
        """ method to read the book 
        
        input_book_path: filepath, url path or book name
        """
        json_book, pages = self.create_json_book(input_book_path, password)
        
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
