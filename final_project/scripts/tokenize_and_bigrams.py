from time import sleep
import os
import re
import collections
import nltk

from nltk.corpus import stopwords

from nltk.tokenize import regexp_tokenize
"""
from nltk.collocations import BigramCollocationFinder
from nltk.metrics import BigramAssocMeasures
from nltk.collocations import TrigramCollocationFinder
from nltk.metrics import TrigramAssocMeasures
"""

punctuation = re.compile(r'[-.?!%,";:()|0-9]')

for a in range(2013,2014):

	sleep(1)
	print "\n...starting %s files" % str(a)

	directory = "../data/text/%s" % str(a)
	files = os.listdir(directory)

	for f in files:

		print f
		print type(f)

		if ".txt" in f:
			try:

				filename = directory + "/" + f
				
				# === Word list and stopwords ===

				word_list = re.split('\s+', open(filename).read().lower())
				words = (punctuation.sub("", word).strip() for word in word_list)
#				words = (word for word in words if word not in stopwords.words('english'))

				stopwords = nltk.corpus.stopwords.words('english')

				# === Bigrams ===
				
				bigrams = nltk.bigrams([w for w in words])

				fdist = nltk.FreqDist(bigrams)
				keys = fdist.keys()
				clean = []

				for bigram in keys:
					if bigram[0] not in stopwords:
						if bigram[1] not in stopwords:
							clean.append(bigram)
				
				print clean

#				bcf = BigramCollocationFinder.from_words(words)
#				print bcf.nbest(BigramAssocMeasures.likelihood_ratio, 10)

			except: 
				pass
