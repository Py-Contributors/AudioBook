import requests
from bs4 import BeautifulSoup


class ArticleWebScraper:
    """
    ArticleWebScraper class

    methods:
        get_json_from_web_article: returns a json from a non-empty <article> tag  # noqa: E501
        get_title_from_article: returns the <title> tag from the html page

    sample usage:
        ab = AudioBook(speed="normal")
        ab.read_book(file_path, password="abcd")
    """

    def __init__(self, article_url):
        page = requests.get(article_url)
        self.article_url = article_url
        self.soup = BeautifulSoup(page.content, "html.parser")

    def get_title_from_article(self):
        """returns the <title> tag from the html page"""
        return self.soup.title.text

    def get_page_data(self):
        """returns a json from a non-empty <article> tag"""
        response = requests.get(self.article_url)

        if response.status_code != 200:
            return None

        soup = BeautifulSoup(response.content, "html.parser")

        text_data = soup.getText().replace("\n", "")
        return text_data
