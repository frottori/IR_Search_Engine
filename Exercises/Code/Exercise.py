# import nltk 
# nltk.download() 

from nltk.book import *
# μας δείχνει τις εμφανίσεις της ζητούμενης λέξης μαζί με κάποιο από το κείμενο μέσα στο οποίο βρίσκεται (context).
text1.concordance("monstrous")  # εμφανίσεις της λέξης monstrous  στο βιβλίο Moby Dick (text1)

# 1. Ψάξτε για άλλες πιθανές λέξεις στο ίδιο βιβλίο 
text1.concordance("Moby")

# 2. Ψάξτε στο βιβλίο Sense and Sensibility για τη λέξη affection
text2.concordance("affection")

# 3. Ψάξτε στο βιβλίο Genesis πότε ή πόσο έζησαν κάποιοι άνθρωποι (π.χ. lived)
text3.concordance("lived")

# άλλες λέξεις που χρησιμοποιούνται με παρόμοιο τρόπο με την λέξη monstrous
text1.similar("monstrous")
text2.similar("monstrous") 

# τα κοινά εννοιολογικά πλαίσιά (context) στα οποίο μπορεί να βρίσκονται δύο ή περισσότερες λέξεις 
text2.common_contexts(["monstrous", "very"])