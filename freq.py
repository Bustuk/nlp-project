import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import *

def normalize_document(doc):
  # Ujednolicenie wielkości liter
  doc = doc.lower()
  
  # Usunięcie znaków interpunkcyjnych
  doc = re.sub(r'[.,;:—–-]', '', doc)
  
  # Usunięcie nawiasów i cudzysłowów
  doc = re.sub(r'[„”“‟”]', '', doc)
  
  # Użycie algorytmu Levenshteina do usunięcia znaków pytajnika, wykrzyknika i wielokropek
  doc = doc.replace('?', '')
  doc = doc.replace('!', '')
  doc = doc.replace('...', '')
  
  return doc

def get_word_freq(text):
  text = normalize_document(text)
  # Tokenize the text
  tokens = nltk.word_tokenize(text, language='english')

  # Remove stop words
  stop_words = stopwords.words('english')

  filtered_tokens = [w for w in tokens if not w in stop_words]

  # Stem words 
  stemmer = SnowballStemmer('english')
  stemmed_tokens = [stemmer.stem(w) for w in filtered_tokens]

  # Create a dictionary of the words and their frequencies
  word_freq = nltk.FreqDist(stemmed_tokens)

  return word_freq