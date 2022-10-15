from audiobook import AudioBook
import unittest


class TestAudioBook(unittest.TestCase):
    def test_invalidPathNumeric(self):
        with self.assertRaises(IOError):
            ab = AudioBook()
            ab.read_book(123)

    def test_openDirectory(self):
        with self.assertRaises(IsADirectoryError):
            ab = AudioBook()
            ab.read_book('/')

    def test_fileDoesNotExist(self):
        with self.assertRaises(FileNotFoundError):
            ab = AudioBook()
            ab.read_book('oiawhgaiurgieurghergerg')

    # def test_fileIsNotPDF(self):
    #     with self.assertRaises(PdfReadError):
    #         ab = AudioBook(__file__)
    #         ab.text_to_speech()
