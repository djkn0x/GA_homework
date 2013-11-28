"""
This script uses NLTK to calculate the trigrams (three word collocations) 
within a text corpus.  

"""

import re
import os
from time import sleep
from collections import Counter
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.collocations import TrigramCollocationFinder
from nltk.metrics import TrigramAssocMeasures 


def stem_word(word):
	"""Takes a single word input and returns the stem."""
	stemmer = PorterStemmer()
	stem = stemmer.stem
	stemmed_word = stem(word)
	return stemmed_word


def calc_trigrams(text, min_freq=50):
	"""Returns frequency of trigrams from a text input."""
	words = [w.lower() for w in text]
	tcf = TrigramCollocationFinder.from_words(words)
	tcf.apply_freq_filter(min_freq)
	trigrams = tcf.ngram_fd.items()
	trigram_list.append(trigrams)
	return trigram_list


year_range = range(2005, 2013)
stops = stopwords.words('english')
blacklist = re.compile(u'[^a-zA-Z0-9 ]+')
fulltext = []

for year in year_range:

	print "\n...starting %s files" % str(year)
	combined = []
	
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
						if len(token) > 3:
							if token not in stops: 
								# stem = stem_word(token)
								combined.append(token)
								fulltext.append(token)

			except: 
				pass
	

	# === Trigrams by year ===
	trigram_list = []
	year_trigrams = calc_trigrams(combined)

	f = open("../data/trigrams/%s_trigrams.txt" % str(year), 'w')
	f.write(str(year_trigrams))
	f.close()


# === Trigrams across entire corpus ===
trigram_list = []
corpus_trigrams = calc_trigrams(fulltext)

f = open("../data/trigrams/corpus_trigrams.txt", 'w')
f.write(str(corpus_trigrams))
f.close()
