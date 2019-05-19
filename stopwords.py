from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from string import punctuation

text = "Do not go gentle into that good night. Old age should burn and rave at close of day;"

stop_words = stopwords.words('english') + list(punctuation)

filtered_tokens = [word for word in word_tokenize(text) if word not in stop_words]

print("Filtered tokens: " + str(filtered_tokens))

