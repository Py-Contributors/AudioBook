#!/bin/bash
check_command() {
    if [ ! -x "$(command -v $1)" ]; then
        echo "$1 is not installed"
        pip install $1
        exit 1
    fi
}

check_directory() {
    if [ ! -d "$1" ]; then
        echo "$1 is not found"
        exit 1
    fi
}

check_file() {
    if [ ! -f "$1" ]; then
        echo "$1 is not found"
        exit 1
    fi
}

# check if the git is installed
check_command git
check_command flake8
check_command twine
check_file setup.py
python3 setup.py sdist bdist_wheel
check_directory dist
python3 -m twine upload dist/*

rm -rf dist
rm -rf build
rm -rf *.egg-info
find . -name "*.pyc" -exec rm -rf {}\;
