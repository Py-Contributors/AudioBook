from audiobook import AudioBook
import unittest
from PyPDF2.utils import PdfReadError


class TestAudioBook(unittest.TestCase):
    def test_invalidPathNumeric(self):
        with self.assertRaises(IOError):
            ab = AudioBook(123)
            ab.text_to_speech()

    def test_openDirectory(self):
        with self.assertRaises(IsADirectoryError):
            ab = AudioBook('/')
            ab.text_to_speech()

    def test_fileDoesNotExist(self):
        with self.assertRaises(FileNotFoundError):
            ab = AudioBook('oiawhgaiurgieurghergerg')
            ab.text_to_speech()

    def test_fileIsNotPDF(self):
        with self.assertRaises(PdfReadError):
            ab = AudioBook(__file__)
            ab.text_to_speech()
