import re 
import os
import string
from nltk.corpus import stopwords
from nltk.collocations import BigramCollocationFinder
from nltk.metrics import BigramAssocMeasures
from collections import defaultdict


def stem_word(word):
	"""Takes a single word input and returns the stem."""
	stemmer = PorterStemmer()
	stem = stemmer.stem
	stemmed_word = stem(word)
	return stemmed_word


def calc_bigrams(text):
	"""Returns frequency of bigrams from a text input."""
	words = [w for w in text]
	bcf = BigramCollocationFinder.from_words(words)
	# bcf.apply_freq_filter(freq)
	bigram_measures = BigramAssocMeasures()
	bigrams = bcf.nbest(bigram_measures.pmi, 100)
	bigram_list.append(bigrams)
	return bigram_list


# def calc_brigrams(text, min_freq=10, n_best=10, scores=False) :

# 	"""Gets N best bigrams from a list of words.
# 	@param min_freq: minimum ngram frequency to keep
# 	@type min_freq: int; default value of 10
# 	@param n_best: number of highest-scored ngrams to return
# 	@type n_best: int
# 	@param scores: return tuples of ngram and scores, or not
# 	@type scores: boolean
# 	"""

# 	bcf = BigramCollocationFinder.from_words(text)
# 	bcf.apply_freq_filter(min_freq)
# 	bigrams = BigramAssocMeasures.likelihood_ratio

# 	if scores is False :
# 		return bcf.nbest(bigrams, n_best)
# 	elif scores is True :
# 		return bcf.score_ngrams(bigrams)[:n_best]


def regex_punc_strip(text):

	"""Strips punctuation from a string. 
	Source: http://stackoverflow.com/questions/265960/best-way-to-strip-punctuation-from-a-string-in-python
	"""

	regex = re.compile('[%s]' % re.escape(string.punctuation))
	return regex.sub('', text)


fulltext = []
bigram_list = []
blacklist = re.compile(u'[^a-zA-Z0-9 ]+')
stops = stopwords.words('english')

year_range = range(2005, 2006)

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
								# token = stem_word(token)
								combined.append(token)
								fulltext.append(token)

			except: 
				pass
	
	# === Bigrams by year ===
	year_bigrams = calc_bigrams(combined)

	f = open("../data/bigrams/%s_bigrams.txt" % str(year), 'w')
	f.write(str(year_bigrams))
	f.close()

# === Bigrams across entire corpus ===
corpus_bigrams = calc_bigrams(fulltext)

f = open("../data/bigrams/corpus_unigrams.txt", 'w')
f.write(str(corpus_bigrams))
f.close()
