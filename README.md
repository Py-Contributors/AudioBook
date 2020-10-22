﻿<p align="center">
  <a href="https://codeperfectplus.github.io/audiobook/"><img src="https://capsule-render.vercel.app/api?type=rect&color=009ACD&height=100&section=header&text=audioBook&fontSize=80%&fontColor=ffffff" alt="website title image"></a>
  <h2 align="center">👉 Listen to any PDF book with just few line of Python code👈</h2>
</p>

<p align="center">
<img src="https://img.shields.io/badge/language-python-blue?style=for-the-badge" alt="repo language">
<a href="https://github.com/codeperfectplus/audiobook/stargazers"><img src="https://img.shields.io/github/stars/codeperfectplus/audiobook?style=for-the-badge" alt="github stars"></a>
<a href="https://github.com/codeperfectplus/audiobook/network/members"><img src="https://img.shields.io/github/forks/codeperfectplus/audiobook?style=for-the-badge" alt="github forks"></a>
<img src="https://img.shields.io/github/languages/code-size/codeperfectplus/audiobook?style=for-the-badge" alt="code size">
  </p>
  <p align="center">
<a href="https://github.com/codeperfectplus/audiobook/issues"><img src="https://img.shields.io/github/issues-raw/codeperfectplus/audiobook?style=for-the-badge" alt="open issues"></a>
<a href="https://github.com/codeperfectplus/audiobook/issues"><img src="https://img.shields.io/github/issues-closed-raw/codeperfectplus/audiobook?style=for-the-badge" alt="closed issues"><a/>
<a href="https://github.com/codeperfectplus/audiobook/pulls"><img src="https://img.shields.io/github/issues-pr-raw/codeperfectplus/audiobook?style=for-the-badge" alt="open pull request"></a>
<a href="https://github.com/codeperfectplus/audiobook/pulls"><img src="https://img.shields.io/github/issues-pr-closed-raw/codeperfectplus/audiobook?style=for-the-badge" alt="closed pull request"></a>
</p>
<p align="center">
<img src="https://img.shields.io/github/hacktoberfest/2020/codeperfectplus/audiobook?style=for-the-badge" alt="hacktoberfest">
<a href="https://raw.githubusercontent.com/codeperfectplus/audiobook/master/LICENSE"><img src="https://img.shields.io/github/license/codeperfectplus/audiobook?style=for-the-badge" alt="MIT license"></a>
</p>
<p align="center">
<a href="https://discord.gg/JfbK3bS"><img src="https://img.shields.io/discord/758030555005714512.svg?label=Discord&logo=Discord&colorB=7289da&style=for-the-badge" alt="discord invite"></a>
<img src="https://img.shields.io/github/last-commit/codeperfectplus/audiobook?style=for-the-badge" alt="last contributions">
<a href="https://api.github.com/repos/codeperfectplus/audiobook/contributors"><img src="https://img.shields.io/github/contributors/codeperfectplus/audiobook?style=for-the-badge" alt="total contributors"></a>
</p>

## Installation

```sh
pip install audiobook
```

```python
from audiobook import AudioBook
ab = AudioBook("file_path")
ab.text_to_speech()
```

### Linux installation requirements

- If you are on a linux system and if the voice output is not working , then :
    Install espeak , ffmpeg and libespeak1 as shown below:

```sh
sudo apt update && sudo apt install espeak ffmpeg libespeak1
```

## Future Updates

- increase/decrease speech speed
- support to more file extensions
