Command line Usage
=========

`AudioBook` can be used as a command line tool and as a library.
only the command line tool is documented here.


Only basic functionality is implemented.  The following features are not yet implemented:

*   `--delete` option
*   `--volume` option
*   `--speed` option
*   `--save_chapterwise` option

Support Format and extraction method
------------

`AudioBook` supports the following formats and extraction methods:

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
------------

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

Get AudioBook version
------------

.. code-block:: bash

    $ audiobook --version


Read a book
------------

.. code-block:: bash

    $ audiobook -p <file_path> -r

Save audio book
------------

.. code-block:: bash

    $ audiobook -p <file_path> -s

Create a json file

.. code-block:: bash

    $ audiobook -p <file_path> -c
