from bs4 import BeautifulSoup
import re

regex = re.compile(r'[\n\r\t]')


def text_preprocessing(input_text):
    preprocessed_text = [regex.sub("", t) for t in input_text]
    preprocessed_text = [re.sub(' +', ' ', t) for t in preprocessed_text]
    return preprocessed_text


def response_to_text(chapter):
    """ fuction to convert response to text

        required for epub files
        maybe required for html files
    """
    soup = BeautifulSoup(chapter, 'html.parser')
    extracted_text = [para.get_text() for para in soup.find_all('p')]
    preprocessed_text = text_preprocessing(extracted_text)
    return ' '.join(preprocessed_text)


def speak_text(engine, text, display=True):
    """ function to speak text and display it """
    if display:
        print(text)
    engine.say(text)
    engine.runAndWait()
