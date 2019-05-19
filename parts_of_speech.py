import nltk

text = "The flying flies flew through the night"

by_parts = nltk.pos_tag(nltk.tokenize.word_tokenize(text))

print("Parts of speech: " + str(by_parts))