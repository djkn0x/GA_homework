import re
import os
from time import sleep
from collections import Counter

import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.collocations import BigramCollocationFinder, TrigramCollocationFinder
from nltk.metrics import BigramAssocMeasures, TrigramAssocMeasures 

year_range = range(2012, 2013)
stops = stopwords.words('english')
blacklist = re.compile(u'[^a-zA-Z0-9 ]+')
combined = []

def stem_word(word):
	stemmer = PorterStemmer()
	stem = stemmer.stem
	stemmed_word = stem(word)
	return stemmed_word

for year in year_range:

	print "\n...starting %s files" % str(year)

	unigram_list = []
	bigram_list = []
	trigram_list = []

	directory = "../data/text/%s" % str(year)
	files = os.listdir(directory)

	for f in files:

		if f.endswith(".txt"):
			try:

				filename = directory + "/" + f
				text = open(filename).read().lower()

				# === Tokenize and stem  ===
				sents = sent_tokenize(text)			
				for sent in sents: 
					s = blacklist.sub('', sent)
					tokens = word_tokenize(s)

					for token in tokens:
						if token not in stops: 
							stem = stem_word(token)
							combined.append(stem)

			except: 
				pass
	
	# === Unigrams ===
	words = [w.lower() for w in combined]
	count = Counter(words).most_common(25)
	print count
	
	# === Bigrams ===
	words = [w.lower() for w in combined]
	bcf = BigramCollocationFinder.from_words(words)
	bigrams = bcf.ngram_fd.items()
	print bigrams[:25]

	# === Trigrams ===
	words = [w.lower() for w in combined]
	tcf = TrigramCollocationFinder.from_words(words)
	trigrams = tcf.ngram_fd.items()
	print trigrams[:25]
