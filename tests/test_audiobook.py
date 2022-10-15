from audiobook import AudioBook
import unittest
from PyPDF2.errors import PdfReadError


class TestAudioBook(unittest.TestCase):
    def test_invalidPathNumeric(self):
        with self.assertRaises(IOError):
            ab = AudioBook('normal')
            ab.txt_to_json(123)

    def test_openDirectory(self):
        with self.assertRaises(IsADirectoryError):
            ab = AudioBook('normal')
            ab.txt_to_json('/')

    def test_fileDoesNotExist(self):
        with self.assertRaises(FileNotFoundError):
            ab = AudioBook('normal')
            ab.txt_to_json('oiawhgaiurgieurghergerg')

    def test_fileIsNotPDF(self):
        with self.assertRaises(PdfReadError):
            ab = AudioBook('normal')
            ab.pdf_to_json(__file__)
