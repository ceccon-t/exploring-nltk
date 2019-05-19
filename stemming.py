import nltk

text = "The flying flies flew through the night"

stemmer = nltk.stem.PorterStemmer()

stemmed_words = [stemmer.stem(word) for word in nltk.tokenize.word_tokenize(text)]

print("Stemmed words: " + str(stemmed_words))