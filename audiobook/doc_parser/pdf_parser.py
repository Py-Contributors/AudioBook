import io
import ast

import PyPDF2

from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage

from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument


class PdfMinerDocParser(object):
    """

    PdfMinor Doc Parser:
        1. get_metadata : get metadata of pdf file
        2. get_text : convert pdf to text
        3. get_toc : get table of contents if available

    """
    def __init__(self):
        self.laparams = LAParams(char_margin=1,
                                 line_margin=0.5,
                                 all_texts=True)

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

            for page in PDFPage.get_pages(fp=fp,
                                          pagenos=pagenos,
                                          maxpages=maxpages,
                                          password=password,
                                          caching=caching):
                interpreter.process_page(page)

            pdf_data = retstr.getvalue()
            return pdf_data

    def get_toc(self, filepath, password=None):
        """ function to get table of contents if available """
        output_toc = []
        # if not os.path.isfile(output_toc_path):
        with open(filepath, 'rb') as fp:
            parser = PDFParser(fp)

            document = PDFDocument(parser, password=password)
            try:
                outlines = document.get_outlines()
                for (level, title, _, _, _) in outlines:
                    output_toc.append((level, title))
                return output_toc
            except Exception as e:
                print(e)
                return output_toc


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
                pdf_data += pageObj.extractText()
        return pdf_data

    def get_toc(self, filepath, password=None):
        outlines = []

        with open(filepath, "rb") as fp:
            pdfReader = PyPDF2.PdfFileReader(fp, strict=False)
            if password:
                pdfReader.decrypt(password)
            outlines = pdfReader.getOutlines()
            if outlines:
                outlines = str(outlines).replace("IndirectObject(", "[")
                outlines = outlines.replace(")", "]").replace("/", "")
                outlines = ast.literal_eval(outlines)

        return outlines
