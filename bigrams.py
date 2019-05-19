from nltk.collocations import *

text = "Do not go gentle into that good night. Old age should burn and rave at close of day;"

finder = BigramCollocationFinder.from_words([word for word in text.split()])

print(sorted(finder.ngram_fd.items()))
