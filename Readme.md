# Project Title
Text Summarizer Application


## Overview

This is a simple Text Summarizer application built using Tkinter, a Python GUI library, and the Natural Language Toolkit (NLTK) for natural language processing tasks. The application allows users to select a text file, view its content, and generate a summary based on the frequency of words in the text.


## Features

Browse File:- Click the "Browse" button to select a text file (.txt).

Text Display:- View the content of the selected text file in a text widget.

Summarize:- Click the "Summarize" button to generate a summary based on word frequency.

Colorful Interface:- The application features a visually appealing interface with color-coded elements.


## Getting Started

### Prerequisites
Python 3.x
NLTK Library
Tkinter Library


# Install the required libraries
pip install nltk


# Run Application
python Summarizer.py


# Import Tinker Library
import tkinter as tk
from tkinter import filedialog


# Additional NLTK Downloads
import nltk 
nltk.download("stopwords") <br>
nltk.download("punkt") <br>


# Libraries for Topic Modeling (Optional)
import gensim
from gensim import corpora <br>
from gensim.models import CoherenceModel <br>


# Dependencies
nltk==3.6.3

# Usage
Launch the application.
Click the "Browse" button to select a text file.
View the content of the text file in the designated area.
Click the "Summarize" button to generate a summary based on word frequency.
The summary will be displayed in the lower text area.


# Acknowledgments

NLTK Library: https://www.nltk.org/
Tkinter Library: https://docs.python.org/3/library/tkinter.html
