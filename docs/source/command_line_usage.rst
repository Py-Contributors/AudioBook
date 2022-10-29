Usages
-----
-----

`AudioBook` can be used as a command line tool and as a library.
only the command line tool is documented here.

Only basic functionality is implemented.  The following features are not yet implemented:

*   `--delete` option
*   `--volume` option
*   `--speed` option
*   `--save_chapterwise` option

=========== ================== ===============
File Format Supported          extraction_engine
=========== ================== ===============
PDF         ✅                 pypdf2/pdfminor
TXT         ✅                 default set                  
EPUB        ✅                 default set                  
MOBI        ✅                 default set                  
HTML        ✅                 default set                  
DOCX        ✅                 default set                  
ODT         ✅                 default set                  
=========== ================== ===============


As command line tool
-----------------

.. code-block:: bash

    $ audiobook --help
    Usage: audiobook [OPTIONS] COMMAND [ARGS]...

    optional arguments:
    -h, --help            show this help message and exit
    -p [PATH], --path [PATH]
                            book file path
    -v, --version         show programs version number and exit
    -l, --library         get all books in library
    -c, --create-json     create json file from input file
    -s, --save-audio      save audio files from input file
    -r, --read-book       read the book from input file

    commands: read, save, create

Read a book

.. code-block:: bash

    $ audiobook -p <file_path> -r

Save audio book

.. code-block:: bash

    $ audiobook -p <file_path> -s

Create a json file

.. code-block:: bash

    $ audiobook -p <file_path> -c

As a library
------------

.. code-block:: python

    from audiobook import AudioBook

    # argument: Speech-Speed="slow/normal/fast", volume = 0.0 to 1.0
    ab = AudioBook(speed="normal", volume=1.0) 


Read a book

.. code-block:: python

    ab.read_book(book_path) 
    # additional parameter:
        #  - password (if book is password protected)
        #  - extraction_engine (default: "pypdf2/pdfminer") for pdf files
    
    # example:

    ab.read_book("book.pdf", password="1234", extraction_engine="pdfminer")

Save audio book

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

Under development
