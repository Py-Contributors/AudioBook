from cgitb import text
import os
import pyttsx3
import PyPDF2
import logging
import requests

from bs4 import BeautifulSoup

html_text_formattings = ["p", "a", "b", "strong", "i", "em", "mark", "small", "del", "ins", "sub", "sup"]

class WebScraper:
    """
    WebScraper class
    
    methods:
        get_text_lines_from_web_article:
        
    sample usage:
        ab = AudioBook(speed="normal")
        ab.read_book(file_path, password="abcd")
    """
    
    def __init__(self, article_url):
        page = requests.get(article_url)
        self.article_url = article_url
        self.soup = BeautifulSoup(page.content, "html.parser")

    def get_title_from_article (self):
        return self.soup.title.text
    
    def get_text_lines_from_web_article (self):
        if hasattr(self.soup, 'article') and self.soup.article is not None: 
            article_text_tag_items = [
                self.soup.article.findChildren(text_formatting , recursive=True) 
                for text_formatting in html_text_formattings
            ]
            text_lines = []
            for article_text_tag_item in article_text_tag_items:
                for article_text_tag in article_text_tag_item:
                    text_line = dict.keys(dict.fromkeys([tag.string for tag in article_text_tag if tag.string is not None])) 
                    text_lines += text_line
            return dict.keys(dict.fromkeys(text_lines))
        else:
            raise ValueError(f"<article> tag not found in {self.article_url}")
