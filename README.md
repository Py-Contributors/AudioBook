# Audio Book

> Read any PDF book with just few line of Python code

## Installation

Create new Virtual ENV:

```sh
pip install audiobook
```

```python
from audiobook import Audiobook
ab = Audiobook("file_path")
ab.text_to_speech()
```

### Linux installation requirements

- If you are on a linux system and if the voice output is not working , then :
    Install espeak , ffmpeg and libespeak1 as shown below:

```sh
sudo apt update && sudo apt install espeak ffmpeg libespeak1
```
