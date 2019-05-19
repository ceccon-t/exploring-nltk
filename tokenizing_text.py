import nltk

text = "Do not go gentle into that good night. Old age should burn and rave at close of day;"

sents = nltk.tokenize.sent_tokenize(text)
print("sent_tokenize: " + str(sents))

words = [nltk.tokenize.word_tokenize(sent) for sent in sents]
print("word_tokenize: " + str(words))

