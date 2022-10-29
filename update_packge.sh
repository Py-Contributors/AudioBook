#!/bin/bash
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

if ! [ -f "setup.py" ]; then
  echo 'Error: setup.py is not found.' >&2
  exit 1
fi

python3 setup.py sdist bdist_wheel

if ! [ -d "dist" ]; then
  echo 'Error: dist folder is not found.' >&2
  exit 1
fi

python3 -m twine upload dist/*

rm -rf dist
rm -rf build
rm -rf *.egg-info
find . -name "*.pyc" -exec rm -rf {}\;
