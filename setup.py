import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open('requirements.txt') as f:
    required = f.read().splitlines()

setuptools.setup(
    name="audiobook",
    version="3.0.1",
    author="CodePerfectPlus",
    author_email="deepak008@live.com",
    description="Listen to your favourite audiobook",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=required,
    url="https://github.com/codePerfectPlus/audiobook",
    keywords="audiobook",
    packages=setuptools.find_packages(),
    project_urls= {
        "Documentation": "https://pycontributors.readthedocs.io/projects/Audiobook/en/latest/",
        "Source": "https://github.com/Py-Contributors/AudioBook",
        "Tracker": "https://github.com/Py-Contributors/AudioBook/issues"
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: Developers",
    ],
    python_requires=">=3.4",
    entry_points={
        "console_scripts": ["audiobook = audiobook.cli:main"],
    },
)
