<p align="center">
  <a href="https://py-contributors.github.io/audiobook/"><img src="https://capsule-render.vercel.app/api?type=rect&color=009ACD&height=100&section=header&text=audioBook&fontSize=80%&fontColor=ffffff" alt="website title image"></a>
  <h2 align="center">👉 Listen to any PDF book with a few lines of Python code👈</h2>
</p>

<p align="center">
<img src="https://img.shields.io/badge/Python-3.8.5-lightgrey?style=for-the-badge" alt="repo language">
<a href="https://github.com/py-contributors/audiobook/stargazers"><img src="https://img.shields.io/github/stars/py-contributors/audiobook?style=for-the-badge" alt="github stars"></a>
<a href="https://github.com/py-contributors/audiobook/network/members"><img src="https://img.shields.io/github/forks/py-contributors/audiobook?style=for-the-badge" alt="github forks"></a>
<img src="https://img.shields.io/github/languages/code-size/py-contributors/audiobook?style=for-the-badge" alt="code size">
  </p>
  <p align="center">
<a href="https://pypi.org/project/audiobook/"><img src="https://img.shields.io/pypi/status/audiobook.svg?style=for-the-badge" alt="pypi status"></a>
<a href="https://pypi.org/project/audiobook/"><img src="https://img.shields.io/pypi/dm/audiobook?style=for-the-badge" alt="download"></a>
<a href="https://pypi.org/project/audiobook/"><img src="https://img.shields.io/readthedocs/audiobook?style=for-the-badge" alt="docs"></a>
<a href="https://pypi.org/project/audiobook/"><img src="https://img.shields.io/librariesio/release/pypi/audiobook?style=for-the-badge" alt="dependices"></a>
</p>
<p align="center">
<a href="https://discord.gg/JfbK3bS"><img src="https://img.shields.io/discord/758030555005714512.svg?label=Discord&logo=Discord&colorB=7289da&style=for-the-badge" alt="discord invite"></a>
<a href="https://api.github.com/repos/py-contributors/audiobook/contributors"><img src="https://img.shields.io/github/contributors/py-contributors/audiobook?style=for-the-badge" alt="total contributors"></a>
</p>

## Installation

Install using [pypi](https://pypi.org/project/audiobook/)

```sh
pip install audiobook
```

```python
from audiobook import AudioBook
# argument: Speech-Speed="slow/normal/fast", volume = 0.0 to 1.0
ab = AudioBook(speed="normal", volume=1.0) 

# if file is password protected, pass password as argument

# save_page_wise audio/whole book in one mp3 file
ab.save_audio(self, input_book_path, password=None, save_page_wise=False): 

ab.read_book(file_path) # listen to the book
ab.create_json_book(file_path) # create json file of the book

ab.get_library() # get all the books in your library
```

## Usages

The audiobook is a python module for listening to your favourite PDF book.

## Test

Run tests:

```sh
pip install -r requirements.txt
python -m unittest tests
```

## Documentation

Read Detailed [Documentation here](https://audiobook.readthedocs.io/)

### Linux Installation Requirements

- If you are using a Linux system and the voice output is not working, then :
    Install espeak , ffmpeg and libespeak1 as shown below:

```sh
sudo apt update && sudo apt install espeak ffmpeg libespeak1
```

## Roadmap

- Speech-Speed Control
- Support more extensions
- Save the audiobook for future

## Project status

This project is currently in development. Any contributions are welcome.

## Changelog

**V2.0.1**

- [x] Mobi file support
- [x] Epub file support
- [x] User can now save the audiobook for future
- [x] User library added    

**V2.0.0**

- [x] Save Audio Book locally
- [x] Listen to the book
- [x] Speech-speed control
- [x] Read password-protected PDF
- [x] Create JSON file for the book  

** Upcoming changes**

- [ ] Change the voice of the narrator
- [ ] Support more extensions


## Author

- Module : AudioBook
- Author  : py-contributors
- Language : Python

<img align="right" src="https://img.shields.io/badge/Made%20with-Python-1f425f.svg?style=for-the-badge">

## Contributors

<a href="https://github.com/Py-Contributors/audiobook/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=Py-Contributors/audiobook"/>
</a>
