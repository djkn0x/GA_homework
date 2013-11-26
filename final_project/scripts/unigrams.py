import re
import os
from collections import Counter
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize

year_range = range(2005, 2013)
stops = stopwords.words('english')
blacklist = re.compile(u'[^a-zA-Z0-9 ]+')
fulltext = []

def stem_word(word):
	"""Takes a single word input and returns the stem."""
	stemmer = PorterStemmer()
	stem = stemmer.stem
	stemmed_word = stem(word)
	return stemmed_word

def calc_unigrams(text, number=100):
	"""Returns frequency of unigrams from a text input."""
	words = [w for w in text]
	count = Counter(words).most_common(number)
	return count

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
	
	# === Unigrams by year ===
	year_unigrams = calc_unigrams(combined, number=5000)

	f = open("../data/unigrams/%s_unigrams.txt" % str(year), 'w')
	f.write(str(year_unigrams))
	f.close()

# === Unigrams across entire corpus ===
corpus_unigrams = calc_unigrams(fulltext, number=5000)

f = open("../data/unigrams/corpus_unigrams.txt", 'w')
f.write(str(corpus_unigrams))
f.close()
