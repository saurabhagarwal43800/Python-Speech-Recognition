from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

print(lemmatizer.lemmatize("better"))          # By default part of speech is set to n -> noun
print(lemmatizer.lemmatize("better",pos='v'))  # v -> verb
print(lemmatizer.lemmatize("better",pos='a'))  # a -> adjective
print(lemmatizer.lemmatize("best"))
print(lemmatizer.lemmatize("best",pos='v'))
print(lemmatizer.lemmatize("best",pos='a'))
print(lemmatizer.lemmatize("good"))
print(lemmatizer.lemmatize("good",pos='v'))
print(lemmatizer.lemmatize("good",pos='a'))

print(lemmatizer.lemmatize("cacti"))
print(lemmatizer.lemmatize("run",pos='v'))




