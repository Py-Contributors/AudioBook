import pyttsx3
import PyPDF2

speed_dict = {
    "slow": 100,
    "normal": 150,
    "fast": 200}

def speak_text(engine, text):
    engine.say(text)
    engine.runAndWait()
    

class AudioBook:
    def __init__(self, speaker=None, speed="medium"):
        self.speaker = speaker
        self.engine = pyttsx3.init()
        self.engine.setProperty("rate", speed_dict[speed])

    def read_book(self, book_path):
        with open(book_path, "rb") as fp:
            pdfReader = PyPDF2.PdfFileReader(fp)
            pages = pdfReader.numPages
            speak_text(self.engine, "The Book has total: " + str(pages) + " pages!")
            speak_text(self.engine, "Please enter the page number: ")
            
            start_page = int(input("Please enter the page number: "))
            speak_text(self.engine, "Reading the book now!")
            
            for num in range(start_page, pages):
                speak_text(self.engine, "Reading page number " + str(num))
                page = pdfReader.getPage(num)
                text = page.extractText()
                speak_text(self.engine, text)

    
