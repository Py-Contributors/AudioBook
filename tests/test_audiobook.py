import unittest

from audiobook import AudioBook


class TestAudioBook(unittest.TestCase):
    def test_invalidPathNumeric(self):  # TODO #41: Update tests
        with self.assertRaises(IOError):
            ab = AudioBook("normal")
            ab.txt_to_json(123)

    def test_openDirectory(self):  # TODO #41: Update tests
        with self.assertRaises(IsADirectoryError):
            ab = AudioBook("normal")
            ab.txt_to_json("/")

    def test_fileDoesNotExist(self):  # TODO #41: Update tests
        with self.assertRaises(FileNotFoundError):
            ab = AudioBook("normal")
            ab.txt_to_json("oiawhgaiurgieurghergerg")

    def test_openDirectory(self):  # noqa: F811  # TODO #41: Update tests
        with self.assertRaises(IsADirectoryError):
            ab = AudioBook()
            ab.read_book("/")

    def test_fileDoesNotExist(self):  # noqa: F811  # TODO #41: Update tests
        with self.assertRaises(FileNotFoundError):
            ab = AudioBook()
            ab.read_book("oiawhgaiurgieurghergerg")
