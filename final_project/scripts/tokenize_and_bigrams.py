import re
import os
from time import sleep

from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.collocations import BigramCollocationFinder
from nltk.metrics import BigramAssocMeasures

year_range = range(2013, 2014)
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
						# if token in english words
						stem = stem_word(token)
						combined.append(stem)

			except: 
				pass


# TO DO: strip punctuation from combined

# === Unigrams ===
# TO DO: strip punctuation from combined


# === Bigrams ===
words = [w.lower() for w in combined]
bcf = BigramCollocationFinder.from_words(words)
# TO DO: strip stopwords from bigrams
bigrams = bcf.nbest(BigramAssocMeasures.likelihood_ratio, 1000)

clean = []
for bigram in bigrams:
	if bigram[0] not in stops:
		if bigram[1] not in stops:
			clean.append(bigram)
print clean


#fdist = nltk.FreqDist(bigrams)
#keys = fdist.keys()
