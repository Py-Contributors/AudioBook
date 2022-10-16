import requests

from bs4 import BeautifulSoup

html_text_formattings = ["p", "a", "b", "strong", "i", "em", "mark", "small", "del", "ins", "sub", "sup"]

class ArticleWebScraper:
    """
    ArticleWebScraper class
    
    methods:
        get_json_from_web_article: returns a json from a non-empty <article> tag
        get_title_from_article: returns the <title> tag from the html page
        
    sample usage:
        ab = AudioBook(speed="normal")
        ab.read_book(file_path, password="abcd")
    """
    
    def __init__(self, article_url):
        page = requests.get(article_url)
        self.article_url = article_url
        self.soup = BeautifulSoup(page.content, "html.parser")

    def get_title_from_article (self):
        """ returns the <title> tag from the html page """
        return self.soup.title.text
    
    def get_json_from_web_article (self):
        """ returns a json from a non-empty <article> tag """
        if hasattr(self.soup, 'article') and self.soup.article is not None: 
            article_text_tag_items = [
                self.soup.article.findChildren(text_formatting , recursive=True) 
                for text_formatting in html_text_formattings
            ]

            json_article = {}
            text_lines = []
            # list(dict.fromkeys(lines))) removes duplicate words in same tag type
            for article_text_tag_item in article_text_tag_items:
                for article_text_tag in article_text_tag_item:
                    text_line = list(dict.fromkeys([tag.string for tag in article_text_tag if tag.string is not None])) 
                    text_lines += text_line
            # list(dict.fromkeys(lines))) removes duplicate words among all tags
            text_lines = list(dict.fromkeys(text_lines))
            for num in range(0, len(text_lines)):
                json_article[num] = text_lines[num]
            return json_article, len(json_article)
        else:
            raise ValueError(f"<article> tag not found in {self.article_url}")
