import nltk
from nltk.book import *
from nltk.draw import *

# Ερώτηση 1α
# i)“Monty Python and the Holy Grail”, πόσο πλούσιο είναι το λεξιλόγιο καθώς και πόσες φορές
# εμφανίζεται η λέξη “LAUNCELOT” και σε τι ποσοστό επί του λεξιλογίου του βιβλίου.
print(len(text6)) # Monty Python Book (text6) length 
print(len(sorted(set(text6)))) # πόσο πλούσιο το λεξιλόγιο 
print(text6.count("LAUNCELOT")) # εμφανίσεις της λέξης LAUNCELOT
perc = (text6.count("LAUNCELOT") / len(text6)) * 100 
print(perc) # ποσοστό επί του λεξιλογίου

# ii)“Chat Corpus”. Πόσο πλούσιο είναι το λεξιλόγιο καθώς και πόσες φορές εμφανίζονται οι
# λέξεις “omg”, “OMG” και “lol” και σε τι ποσοστό επί του λεξιλογίου του βιβλίου.

print(len(text5))   # Chat Corpus (text5) length
print(len(sorted(set(text5)))) # πόσο πλούσιο το λεξιλόγιο 
print(text5.count("omg")) 
print(text5.count("OMG"))
print(text5.count("lol"))
perc = (text5.count("omg") / len(text5)) * 100
print(perc) # ποσοστό επί του λεξιλογίου

# Εμφάνιση της κατανομής των λέξεων στο text4
text4.dispersion_plot(["citizens", "democracy", "freedom", "duties", "America"]) 
text4.dispersion_plot(["war", "voters", "peace", "Iraq", "terrorism"]) 
# Ερώτηση 1β
# Για καθένα από τα παραπάνω βιβλία επιλέξτε τρεις ακόμα λέξεις (αντιπροσωπευτικές
# ή μη) υπολογίζοντας το ποσοστό χρήσης της καθεμίας επί του λεξιλογίου του κάθε βιβλίου.

print(sent1) # θα εμφανίσει την πρώτη πρόταση από το βιβλίο 1

# Για να υπολογίσουμε την κατανομή συχνότητας (frequency distribution) κάθε στοιχείου του
# λεξιλογίου σε ένα κείμενο text, χρησιμοποιούμε την εντολή του NLTK FreqDist(text)και
# freq_dist.most_common(number)

fdist1 = FreqDist(text1) #Βάλε στην μεταβλητή fdist1 την κατανομή συχνότητας στο text1
print(fdist1) #Δείξε μου την μεταβλητή fdist1
print(fdist1.most_common(50)) #Εμφάνισε τα 50 στοιχεία που εμφανίζονται με τη μεγαλύτερη συχνότητα
fdist1.plot(50)

sents() # Εμφανίζει την πρώτη πρόταση από κάθε βιβλίο (corpus)
print(sent1) # Εμφανίζει την πρώτη πρόταση από το πρώτο βιβλίο 
print(sent2) # Εμφανίζει την πρώτη πρόταση από το δεύτερο βιβλίο

tokens1=sent1 #βάλε την sent1 στην μεταβλητή token1 normalized
normalized_sent1=[x.lower() for x in tokens1] #για κάθε x που υπάρχει_στο token1 κάνε "μικρά" τα γράμματαnormalized
print(normalized_sent1)

print(len(sent1))
print(len(normalized_sent1))
print(len(set(sent1)))          # tokenizes sent1 with no duplicates like hello becomes "h" "e" "l" "o"
print(len(set(normalized_sent1)))

# Stemming
# Βάλτε στη μεταβλητή tokens1 τις πρώτες 200 λεκτικές μονάδες του βιβλίου “Sense and Sensibility”
porter = nltk.PorterStemmer()
[porter.stem(t) for t in tokens1]

# Lemmatization
# χρησιμοποιεί το Wordnet σαν βιβλιοθήκη, ώστε να αντιστοιχίσει (mapping) κάποιες λέξεις με κοινό νόημα.
wnl = nltk.WordNetLemmatizer()
[wnl.lemmatize(t) for t in tokens1]

# Tokenization
sentence = "Monticello wasn't designated as UNESCO World Heritage Siteuntil 1987."
print(sentence.split()) # παρατηρούμε ότι στο τέλος δεν χώρισε το 1987 με την τελεία, κάτι που είναι λάθος.

import nltk.tokenize
tokens = nltk.word_tokenize(sentence)
print(tokens) # πιο σωστός διαχωρισμός των λέξεων

# Αφαίρεση σημείων στίξης και προθημάτων (stop words)
import string
print(string.punctuation) # εμφανίζει τα σημεία στίξης

# Αφαίρεση σημείων στίξης απο τα tokens
cleaned_tokens=[]
for token in tokens:
    if token not in string.punctuation:
        cleaned_tokens.append(token)
print(cleaned_tokens)

# Για να δείτε τα προθήματα της Αγγλικής γλώσσας
stopwords = nltk.corpus.stopwords.words('english')
print(stopwords)

# Αφαίρεση προθημάτων απο τα tokens
cleaned_tokens=[]
for token in tokens:
    if token not in stopwords:
        cleaned_tokens.append(token)
print(cleaned_tokens)