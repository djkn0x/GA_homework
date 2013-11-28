"""
This script prints out the number of words in text files within a directory.  

"""

import os

directory = "../data/corpus"
files = os.listdir(directory)

for f in files:

	if f.endswith(".txt"):
		try:

			print "\n...starting %s" % f
			filename = directory + "/" + f
			text = open(filename).read()
			print len(text.split(' '))

		except: 
			pass
