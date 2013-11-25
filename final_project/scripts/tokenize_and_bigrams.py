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

year_range = range(2005, 2013)
stops = stopwords.words('english')
# stopwords = filter(lambda w: not w.startswith("#"), stopwords)
# [word for word in words if word[0].isupper() ]
blacklist = re.compile(u'[^a-zA-Z0-9 ]+')
fulltext = []
bigram_list = []
trigram_list = []

def stem_word(word):
	"""Takes a single word input and returns the stem."""
	stemmer = PorterStemmer()
	stem = stemmer.stem
	stemmed_word = stem(word)
	return stemmed_word

def calc_bigrams(text):
	"""Returns frequency of bigrams from a text input."""
	words = [w.lower() for w in text]
	bcf = BigramCollocationFinder.from_words(words)
	bigrams = bcf.ngram_fd.items()
	bigram_list.append(bigrams)
	return bigram_list

def calc_trigrams(text):
	"""Returns frequency of trigrams from a text input."""
	words = [w.lower() for w in text]
	tcf = TrigramCollocationFinder.from_words(words)
	trigrams = tcf.ngram_fd.items()
	trigram_list.append(trigrams)
	return trigram_list

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
								stem = stem_word(token)
								combined.append(stem)
								fulltext.append(stem)

			except: 
				pass
	
	# === Unigrams ===
	# words = [w.lower() for w in combined]
	# count = Counter(words).most_common(25)
	# print count
	
	# calc_bigrams(combined)
	# calc_trigrams(combined)

full_bigram_list = calc_bigrams(fulltext)
print full_bigram_list[:50]

full_trigram_list = calc_trigrams(fulltext)
print full_trigram_list[:50]
