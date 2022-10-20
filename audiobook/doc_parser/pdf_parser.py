import io

import PyPDF2

from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage


class PdfMinerDocParser(object):
    """

    PdfMinor Doc Parser:
        1. get_metadata : get metadata of pdf file
        2. get_text : convert pdf to text
        3. get_toc : get table of contents if available

    """
    def __init__(self):
        self.laparams = LAParams(char_margin=1, line_margin=0.5, all_texts=True)

    def get_metadata(self):
        pass

    def get_text(self, filepath, password=None, maxpages=0, caching=True):
        """ function to read all the text from pdf file """
        pagenos = set()
        rsrcmgr = PDFResourceManager()
        retstr = io.StringIO()

        device = TextConverter(rsrcmgr, retstr, laparams=self.laparams)

        with open(filepath, 'rb') as fp:
            interpreter = PDFPageInterpreter(rsrcmgr, device)

            for page in PDFPage.get_pages(fp=fp, pagenos=pagenos, maxpages=maxpages, password=password, caching=caching):
                interpreter.process_page(page)

            pdf_data = retstr.getvalue()
            return pdf_data


class PyPDF2DocParser(object):
    """
    PyPdf2 Doc Parser:

    methods:
        1. get_metadata : get metadata of pdf file
        2. get_text : convert pdf to text
        3. get_toc : get table of contents if available

    """
    def __init__(self):
        pass

    def get_metadata(self):
        pass

    def get_text(self, filepath, password=None, maxpages=0):
        """ function to read all the text from pdf file """
        pdf_data = ""
        with open(filepath, "rb") as fp:
            pdfReader = PyPDF2.PdfFileReader(fp)
            if password:
                pdfReader.decrypt(password)
            num_pages = pdfReader.numPages
            if maxpages:
                num_pages = min(num_pages, maxpages)
            for i in range(num_pages):
                pageObj = pdfReader.getPage(i)
                pdf_data += pageObj.extractText()  # BUG: Page 1Page 2Page 3Page 4Page 5
        return pdf_data
