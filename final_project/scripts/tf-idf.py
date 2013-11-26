from sklearn.feature_extraction.text import CountVectorizer

train_set = ("The sky is blue.", "The sun is bright.")
test_set = ("The sun in the sky is bright.", "We can see the shining sun, the bright sun.")

count_vectorizer = CountVectorizer()
count_vectorizer.fit_transform(train_set)
# print "Vocabulary:", count_vectorizer.vocabulary

freq_term_matrix = count_vectorizer.transform(test_set)
print freq_term_matrix.todense()

# filename = "/Users/dk/Desktop/test_corpus.txt"
# for each file
# corpus = open(filename, 'r').read()
