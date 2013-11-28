"""
This script uses regular expressions and string.punctuation to strip all 
punctuation from a given text file. 

"""

import re 
import string


def regex_punc_strip(text):
	regex = re.compile('[%s]' % re.escape(string.punctuation))
	return regex.sub('', text)


filename = "/Users/dk/Desktop/test_corpus.txt"
text = open(filename).read()

new_text = regex_punc_strip(text)

# save new_text to file
f = open("/Users/dk/Desktop/new_corpus.txt", 'w')
f.write(str(new_text))
f.close()
