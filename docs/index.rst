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