# Need to remove special characters from text file
# e.g. need to convert "se-\nlective" to "selective"
# by removing the -\n

import os
import re

year_range = range(2013, 2014)

for year in year_range:

	directory = "../data/text/%s" % str(year)
	files = os.listdir(directory)

	for f in files:

		if ".txt" in f:
			try:

				# open file
				filename = directory + "/" + f
				text = open(filename).read().lower()

				# convert file from string to list
				textlist = []
				textlist.append(text)

				# replace special characters via regex

				# save file again

			except:
				pass


"""

Replacements to make:
"-\n" ""
"-\n\n" ""
"\n\n" " "
"\n" " "
"\xe2\x80\x99" "'"
"\xef\xac\x81" "fi"
"\xef\xac\x80" "ff"
"pro ject" "project"

"""
