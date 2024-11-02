from collections import defaultdict
import json

def create_inverted_index(stemmed_data):
    inverted_index = defaultdict(list)
    
    for doc_id, words in stemmed_data:
        for word in words:
            if doc_id not in inverted_index[word]:
                inverted_index[word].append(doc_id)
    
    return inverted_index

with open('Files/wiki_data_clean.json', 'r') as file:
    wiki_data = json.load(file)

# Data for invert index
stemmed_data = []
for i, entry in enumerate(wiki_data):
    doc_id = i + 1 
    cleaned_tokens = entry.get("cleaned_tokens", [])
    stemmed_data.append((doc_id, cleaned_tokens))

inverted_index = create_inverted_index(stemmed_data)

for term, doc_ids in inverted_index.items():
    print(f"'{term}': {doc_ids}")
