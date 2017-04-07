"""
The flask application package.
"""
import logging
from pprint import pprint
from collections import defaultdict
from gensim import corpora, models, similarities
#from pattern.en import mood, modality, wordnet
from os import listdir
from os.path import isfile, join
from textblob import Word
from textblob import TextBlob
import nltk
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import sent_tokenize, word_tokenize, RegexpTokenizer
from flask import Flask, jsonify, render_template, request, session

app = Flask(__name__, static_url_path = "/static", static_folder = "static")


@app.route('/')
def index():        
    return render_template('index.html')

if __name__ == '__main__':
    #app.secret_key = 'RAUNAK123'
app.run()
