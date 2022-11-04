import unittest
import json

from audiobook import AudioBook


def load_json(filename):
    with open(filename, "r") as fp:
        return json.load(fp)


output = load_json("assets/output.json")
output_txt = (output['extracted_txt'], {'book_name': 'sample', 'pages': 1})

ab = AudioBook(speed="normal")


class TestAudioBook(unittest.TestCase):

    def test_txt_to_json_pdf_miner(self):
        self.assertEqual(ab.create_json_book("assets/sample.txt"), output_txt)

    def test_pdf_to_json_pdf_miner(self):
        self.assertEqual(ab.create_json_book("assets/sample.pdf", extraction_engine="pdfminer"), output_txt)

    def test_pdf_to_json_pypdf2(self):
        self.assertEqual(ab.create_json_book("assets/sample.pdf", extraction_engine="pypdf2"), output_txt)

    def test_odt_to_json(self):
        self.assertEqual(ab.create_json_book("assets/sample.odt"), output_txt)

    def test_mobi_to_json(self):
        self.assertEqual(ab.create_json_book("assets/sample.mobi"), output_txt)

    # def test_docs_to_json(self):
    #     self.assertEqual(ab.create_json_book("assets/sample.doc"), (output['docs'], {'book_name': 'sample', 'pages': 1}))

    # def test_epub_to_json(self): # epub test failing
    #     self.assertEqual(ab.create_json_book("assets/sample.epub"), (output['epub'], {'book_name': 'sample', 'pages': 1}))
