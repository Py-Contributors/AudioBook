from datetime import datetime

project = 'audiobook'
author = 'Deeapk Raj'
release = '3.0.2'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.viewcode',
    'rst2pdf.pdfbuilder',
    'sphinx.ext.autosectionlabel'
]

pdf_documents = [('index', u'documentation', 'My Docs', u'Me'), ]

releases_github_path = "Py-Contributors/AudioBook"

autosectionlabel_prefix_document = True

templates_path = ['_templates']
source_suffix = ".rst"
master_doc = "index"
year = datetime.now().year
copyright = "{} Deepak Raj".format(year)

html_theme = 'sphinx_rtd_theme'  # 'pydata_sphinx_theme' 'alabaster'

html_static_path = ['_static']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', '.venv']
html_sidebars = {'**': ['globaltoc.html', 'relations.html', 'sourcelink.html', 'searchbox.html']}
