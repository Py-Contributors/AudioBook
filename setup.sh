#!/bin/sh

# Setup.sh for linux (tested on Ubuntu 18.04)
echo "Setting up environment for build proces"

# check if the python3 is installed
if ! [ -x "$(command -v python3)" ]; then
  echo 'Error: python3 is not installed.' >&2
  exit 1
fi

# check if the pip3 is installed
if ! [ -x "$(command -v pip3)" ]; then
  echo 'Error: pip3 is not installed.' >&2
  exit 1
fi

# check if python3-dev is installed
if ! [ -x "$(command -v python3-dev)" ]; then
  echo 'Error: python3-dev is not installed.' >&2
  sudo apt-get install python3-dev
fi

sudo apt update && sudo apt install espeak ffmpeg libespeak1

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt