from nltk.corpus import wordnet
from nltk.wsd import lesk
from nltk.tokenize import word_tokenize

print("Definitions: ")
for synset in wordnet.synsets('age'):
    print(synset, synset.definition())

text_time = "Old age should burn and rave"

text_history = "We live in the age of humans"

sense_time = lesk(word_tokenize(text_time), 'age')

sense_history = lesk(word_tokenize(text_history), 'age')

print("First sense: ")
print(sense_time, sense_time.definition())

print("Second sense: ")
print(sense_history, sense_history.definition())