<p align="center">
  <a href="https://codeperfectplus.github.io/audiobook/"><img src="https://capsule-render.vercel.app/api?type=rect&color=009ACD&height=100&section=header&text=audioBook&fontSize=80%&fontColor=ffffff" alt="website title image"></a>
  <h2 align="center">👉 Listen to any PDF book with just a few line of Python code👈</h2>
</p>

<p align="center">
<img src="https://img.shields.io/github/pipenv/locked/python-version/codeperfectplus/audiobook?style=for-the-badge" alt="repo language">
<a href="https://github.com/codeperfectplus/audiobook/stargazers"><img src="https://img.shields.io/github/stars/codeperfectplus/audiobook?style=for-the-badge" alt="github stars"></a>
<a href="https://github.com/codeperfectplus/audiobook/network/members"><img src="https://img.shields.io/github/forks/codeperfectplus/audiobook?style=for-the-badge" alt="github forks"></a>
<img src="https://img.shields.io/github/languages/code-size/codeperfectplus/audiobook?style=for-the-badge" alt="code size">
  </p>
  <p align="center">
<a href="https://pypi.org/project/audiobook/"><img src="https://img.shields.io/pypi/status/audiobook.svg?style=for-the-badge" alt="pypi status"></a>
<a href="https://pypi.org/project/audiobook/"><img src="https://img.shields.io/pypi/dm/audiobook?style=for-the-badge" alt="download"></a>

</p>
<p align="center">
<a href="https://discord.gg/JfbK3bS"><img src="https://img.shields.io/discord/758030555005714512.svg?label=Discord&logo=Discord&colorB=7289da&style=for-the-badge" alt="discord invite"></a>
<img src="https://img.shields.io/github/last-commit/codeperfectplus/audiobook?style=for-the-badge" alt="last contributions">
<a href="https://api.github.com/repos/codeperfectplus/audiobook/contributors"><img src="https://img.shields.io/github/contributors/codeperfectplus/audiobook?style=for-the-badge" alt="total contributors"></a>
</p>

## Installation

Install it from [pypi](https://pypi.org/project/audiobook/)

```sh
pip install audiobook
```

```python
from audiobook import AudioBook
ab = AudioBook("file_path")
ab.text_to_speech()
```

## Usages

The audiobook is a python module to listen to your fav pdf book.

## Documentation

Read Detailed [Documentation here](https://audiobook.readthedocs.io/)

### Linux installation requirements

- If you are on a linux system and if the voice output is not working , then :
    Install espeak , ffmpeg and libespeak1 as shown below:

```sh
sudo apt update && sudo apt install espeak ffmpeg libespeak1
```

## Roadmap

- speech speed control
- Support more extensions
- save the audiobook for future

## Project status

- Alpha

## Author

- Module : AudioBook
- Author  : CodePerfectPlus
- Language : Python

<img align="right" src="https://img.shields.io/badge/Made%20with-Python-1f425f.svg?style=for-the-badge">