import logging
import os

import pyttsx3
from tqdm import tqdm

from audiobook.config import speed_dict
from audiobook.utils import (
    docs_to_json,
    epub_to_json,
    html_to_json,
    load_json,
    mobi_to_json,
    odt_to_json,
    pdf_to_json,
    speak_text,
    txt_to_json,
    write_json_file,
)

logger = logging.getLogger("PyPDF2")
logger.setLevel(logging.INFO)

expand_usr = os.path.expanduser("~")
BOOK_DIR = os.path.join(expand_usr, "audiobook/library")
os.makedirs(BOOK_DIR, exist_ok=True)


class AudioBook(object):
    """
    AudioBook class

    methods:
        get_library: get all books in library
        create_json_book: Creates json book from input file by calling respective method  # noqa: E501
        save_audio: method to save audio files in folder
        read_book: reads the book

    sample usage:
        ab = AudioBook(speed="normal")
        ab.read_book(file_path, password="abcd")
    """

    def __init__(self, speed="normal", volume=1.0):
        self.__engine = pyttsx3.init()
        self.__engine.setProperty("rate", speed_dict[speed])
        self.__engine.setProperty("volume", volume)

    def get_library(self):
        """get all books in library"""
        total_books = os.listdir(BOOK_DIR)
        if len(total_books) == 0:
            return "You have no books in your library"
        print(
            "You Have total {} books in your library".format(len(total_books))
        )
        return total_books

    def create_json_book(self, input_book_path, password=None, extraction_engine=None, load_from_library=False):
        """method to create json book from input file
        it calls respective method based on file format"""
        json_filename = (
            os.path.basename(input_book_path).split(".")[0] + ".json"
        )

        if load_from_library:
            print("Loading book from library")
            if os.path.exists(os.path.join(BOOK_DIR, json_filename)):
                metadata = {"book_name": json_filename.split(".")[0]}
                print("Book already exists in library, reading from library")
                json_book = load_json(os.path.join(BOOK_DIR, json_filename))
                metadata["pages"] = len(json_book)
                return json_book, metadata

        elif input_book_path.endswith(".odt"):
            json_book, metadata = odt_to_json(input_book_path)
        elif input_book_path.endswith(".pdf"):
            json_book, metadata = pdf_to_json(input_book_path, password, extraction_engine=extraction_engine)
        elif input_book_path.endswith(".txt"):
            json_book, metadata = txt_to_json(input_book_path)
        elif input_book_path.endswith(".epub"):
            json_book, metadata = epub_to_json(input_book_path)
        elif input_book_path.endswith(".mobi"):
            json_book, metadata = mobi_to_json(input_book_path)
        elif input_book_path.startswith(("http", "https")):
            json_book, metadata = html_to_json(input_book_path)
        elif input_book_path.endswith((".docx", ".doc")):
            json_book, metadata = docs_to_json(input_book_path)
        else:
            raise NotImplementedError("Only PDF, TXT, EPUB, MOBI, ODT, HTTP, DOCX and DOC files are supported")

        write_json_file(json_book, os.path.join(BOOK_DIR, json_filename))

        return json_book, metadata

    def save_audio(self, input_book_path, password=None, save_page_wise=False, extraction_engine=None):
        """method to save audio files in folder"""

        json_book, metadata = self.create_json_book(input_book_path, password, extraction_engine)

        book_name = metadata["book_name"]
        book_dir = os.path.join(BOOK_DIR, book_name)
        os.makedirs(book_dir, exist_ok=True)

        print("Saving audio files in folder: {}".format(book_dir))

        if save_page_wise:
            for page_num, text in tqdm(json_book.items()):
                self.__engine.save_to_file(
                    text,
                    os.path.join(
                        book_name,
                        book_name + "_page_" + (str(page_num)) + ".mp3",
                    ),
                )
                self.__engine.runAndWait()

        elif not save_page_wise:
            all_text = " ".join([text for text in json_book.values()])
            self.__engine.save_to_file(
                all_text, os.path.join(book_name, book_name + ".mp3")
            )
            self.__engine.runAndWait()

    def read_book(self, input_book_path, password=None, extraction_engine=None):
        """method to read the book

        input_book_path: filepath, url path or book name
        """
        json_book, metadata = self.create_json_book(input_book_path, password, extraction_engine)

        pages = metadata["pages"]

        speak_text(self.__engine, f"The book has total {str(pages)} pages!")
        speak_text(
            self.__engine, "Please enter the page number: ", display=False
        )
        start_page = int(input("Please enter the page number: ")) - 1

        reading = True
        while reading:
            if start_page > pages or start_page < 0:
                speak_text(self.__engine, "Invalid page number!")
                speak_text(
                    self.__engine, f"The book has total {str(pages)} pages!"
                )
                start_page = int(input("Please enter the page number: "))

            speak_text(self.__engine, f"Reading page {str(start_page+1)}")
            pageText = json_book[str(start_page)]
            speak_text(self.__engine, pageText, display=False)

            input_message = "Please Select an option: \n "
            "1. Type 'r' to read again: \n "
            "2. Type 'p' to read previous page\n "
            "3. Type 'n' to read next page\n "
            "4. Type 'q' to quit:\n "
            "5. Type page number to read that page:\n"

            user_input = input(input_message)
            if user_input == "r":
                speak_text(self.__engine, f"Reading page {str(start_page+1)}")
                continue
            elif user_input == "p":
                speak_text(self.__engine, "Reading previous page")
                start_page -= 1
                continue
            elif user_input == "n":
                speak_text(self.__engine, "Reading next page")
                start_page += 1
                continue
            elif user_input == "q":
                speak_text(self.__engine, "Quitting the book!")
                break
            elif user_input.isnumeric():
                start_page = int(user_input) - 1
            else:
                user_input = input(input_message)
                continue
