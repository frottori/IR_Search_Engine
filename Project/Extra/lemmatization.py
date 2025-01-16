
from nltk.tokenize import word_tokenize
import nltk 

tokens = []
lemmed_data = []

wnl = nltk.WordNetLemmatizer()

for d in collected_data:
    tokens = word_tokenize(d['content'])
    lemmed_tokens = [wnl.lemmatize(t) for t in tokens]
    lemmed_data.append({
        "title": d["title"],
        "lemmed_tokens": lemmed_tokens
    })
lemmed_data[1]