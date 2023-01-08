import gensim
import gensim.downloader as api
from gensim.utils import simple_preprocess
from gensim.parsing.preprocessing import STOPWORDS

class WMD:
  def __init__(self):
    # Load the model from the Google News dataset - if not present, download it
    self.model = api.load("word2vec-google-news-300", return_path=False)

  def preprocess(self, doc):
    # Remove stopwords, tokenize and lemmatize
    return [word for word in simple_preprocess(doc) if word not in STOPWORDS]

  def get_similarity(self, text1, text2):
    doc1_tokens = self.preprocess(text1)
    doc2_tokens = self.preprocess(text2)
    # Calculate the Word Mover's Distance between the documents
    distance = self.model.wmdistance(doc1_tokens, doc2_tokens)
    print(f"Word mover's distance: (0 - best, ∞ - worst ) {distance}")
    return distance


