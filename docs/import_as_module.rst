import as module
=========

.. code-block:: python

    from audiobook import AudioBook

    # argument: Speech-Speed="slow/normal/fast", volume = 0.0 to 1.0
    ab = AudioBook(speed="normal", volume=1.0) 


Read a book
------------

.. code-block:: python

    ab.read_book(book_path) 
    # additional parameter:
        #  - password (if book is password protected)
        #  - extraction_engine (default: "pypdf2/pdfminer") for pdf files
    
    # example:

    ab.read_book("book.pdf", password="1234", extraction_engine="pdfminer")

Save audio book
------------

.. code-block:: python

    ab.save_book(book_path, save_page_wise=False)
    # additional parameter:
        #  - password (if book is password protected)
        #  - extraction_engine (default: "pypdf2/pdfminer") for pdf files
        #  - save_page_wise (default: False)
        #  - extraction_engine (default: "pypdf2/pdfminer") for pdf files

    # example:

    ab.save_book("book.pdf", password="1234", save_chapterwise=True, extraction_engine="pdfminer")


save book as txt file
------------

Under development
