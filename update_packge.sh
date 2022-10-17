#!/bin/bash

# Update package on pypi server

# check for flake8 and twine and install if not present
if ! [ -x "$(command -v flake8)" ]; then
    echo 'Error: flake8 is not installed.' >&2
    echo 'Installing flake8...'
    pip install flake8
fi

if ! [ -x "$(command -v twine)" ]; then
    echo 'Error: twine is not installed.' >&2
    echo 'Installing twine...'
    pip install twine
fi

# check for setup.py
if ! [ -f "setup.py" ]; then
  echo 'Error: setup.py is not found.' >&2
  exit 1
fi


# run sdists and wheels
python3 setup.py sdist bdist_wheel

# check for dist folder
if ! [ -d "dist" ]; then
  echo 'Error: dist folder is not found.' >&2
  exit 1
fi


read -p "Do you want to upload to pypi? (y/n) " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]
then
    python3 -m twine upload dist/*
fi


# remove dist folder
rm -rf dist

# remove build folder
rm -rf build

# remove .egg-info folder
rm -rf *.egg-info

# remove .pyc files
find . -name "*.pyc" -exec rm -rf {} \;
