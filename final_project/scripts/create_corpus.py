"""
This script uses stopwords (from nltk.corpus), nltk.stem and nltk.tokenize to clean up text files and 
convert them into a usable corpus.  

"""

import re
import os
from time import sleep

import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize

stops = stopwords.words('english')
punctuation = re.compile(u'[^a-zA-Z ]+')
year_range = range(2005, 2013)
full_corpus = []

def stem_word(word):
	"""Takes a single word input and returns the stem."""
	stemmer = PorterStemmer()
	stem = stemmer.stem
	stemmed_word = stem(word)
	return stemmed_word

for year in year_range:

	print "\n...starting %s files" % str(year)

	annual_corpus = []
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
					s = punctuation.sub('', sent)
					tokens = word_tokenize(s)

					for token in tokens:
						if len(token) > 3:
							if token not in stops: 
								stem = stem_word(token)
								annual_corpus.append(stem)
								full_corpus.append(stem)

			except: 
				pass
	
	# save annual_corpus to file
	f = open("../data/text/%s_corpus.txt" % str(year), 'w')
	f.write(str(annual_corpus))
	f.close()

# save full_corpus to file
f = open("../data/text/full_corpus.txt", 'w')
f.write(str(full_corpus))
f.close()
