import os
import pyttsx3
import PyPDF2
import logging

logging.basicConfig()

from audiobook.article_web_scraper import WebScraper

logger = logging.getLogger("PyPDF2")
logger.setLevel(logging.INFO)

supported_file_types = (".pdf",  ".txt")

speed_dict = {
    "slow": 100,
    "normal": 150,
    "fast": 200}


def speak_text(engine, text, display=True):
    if display:
        print(text)
    engine.say(text)
    engine.runAndWait()

html_text_formattings = ["p", "a", "b", "strong", "i", "em", "mark", "small", "del", "ins", "sub", "sup"]

class AudioBook:
    """
    AudioBook class
    
    methods:
        file_check: checks if file exists
        pdf_to_json: converts pdf to json format
        create_json_book: Creates json book from input file by calling respective method
        save_audio: saves audio files in folder
        read_book: reads the book
        read_web_article: read web article from a given url
        save_web_article: save web article to a .mp3 file from a given url
        
    sample usage:
        ab = AudioBook(speed="normal")
        ab.read_book(file_path, password="abcd")
    """
    
    def __init__(self, speed="normal"):
        self.engine = pyttsx3.init()
        self.engine.setProperty("rate", speed_dict[speed])
    
    def file_check(self, file_path):
        """ 
        checks file format and if file exists
        """
        if not os.path.exists(file_path):
            raise FileNotFoundError("File not found!")

        if not file_path.endswith(supported_file_types):
            raise ValueError("File format not supported!")
      
    def pdf_to_json(self, input_file_path, password=None):
        """ sub method to create json book from pdf file"""
        json_book = {}
        with open(input_file_path, "rb") as fp:
            pdfReader = PyPDF2.PdfFileReader(fp)
            if pdfReader.isEncrypted:
                logging.info("File is encrypted, trying to decrypt...")
                pdfReader.decrypt(password)
            pages = pdfReader.numPages
            for num in range(0, pages):
                pageObj = pdfReader.getPage(num)
                text = pageObj.extractText()
                json_book[num] = text
        return json_book, pages
    
    def txt_to_json(self, input_file_path):
        """ sub method to create json book from txt file """
        json_book = {}
        with open(input_file_path, "r") as fp:
            file_data = fp.read()
        
        # split text into pages of 2000 characters
        for i in range(0, len(file_data), 2000):
            json_book[i] = file_data[i:i+2000]
        return json_book, len(json_book)
        
    def create_json_book(self, input_file_path, password=None):
        """ method to create json book from input file 
            it calls respective method based on file format """
        self.file_check(input_file_path)
        if input_file_path.endswith(".pdf"):
            json_book, pages = self.pdf_to_json(input_file_path, password)
        elif input_file_path.endswith(".txt"):
            json_book, pages = self.txt_to_json(input_file_path)
        return json_book, pages
    

    def save_audio(self, input_file_path, password=None):
        """ method to save audio files in folder """
        self.file_check(input_file_path)
        logging.info("Creating your audiobook... Please wait...")
        json_book, pages = self.create_json_book(input_file_path, password)
        
        book_name = os.path.basename(input_file_path).split(".")[0]
        os.makedirs(book_name, exist_ok=True)
        logging.info('Saving audio files in folder: {}'.format(book_name))
        
        for page_num, text in json_book.items():
            self.engine.save_to_file(text, os.path.join(book_name, book_name + "_page_" + (str(page_num+1) + ".mp3")))
            self.engine.runAndWait()
                
    
    def read_book(self, input_file_path, password=None):
        """ method to read the book """
        self.file_check(input_file_path)
        logging.info("Creating your audiobook... Please wait...")
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
            pageText = json_book[start_page]
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

    def read_web_article(self, article_url):
        """ read web article from a article_url containing an <article> tag """
        ws = WebScraper(article_url)
        text_lines = ws.get_text_lines_from_web_article()
        if len(text_lines) > 0:
            logger.info(f'reading {len(text_lines)} from {article_url}')
            speak_text(self.engine, ws.get_title_from_article(), display=False)
            speak_text(self.engine, ''.join(text_lines), display=False)
        else:
            raise ValueError("<article> tag has no text.")
    
    def save_web_article(self, article_url):
        """ save web article from a article_url containing an <article> tag """
        ws = WebScraper(article_url)
        text_lines = ws.get_text_lines_from_web_article()
        if len(text_lines) > 0:
            title = ws.get_title_from_article()
            mp3_file = os.path.join(os.getcwd(), f"{title}.mp3")
            logger.info(f'saving {article_url} to {mp3_file}')
            self.engine.save_to_file(title+"".join(text_lines), mp3_file)
            self.engine.runAndWait()
        else:
            raise ValueError("<article> tag has no text.")
        

        
