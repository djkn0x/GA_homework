"""
This script prints out the number of text files within a series of directories.  

"""

import os

year_range = range(2005, 2013)
cs229 = 0
nips = 0

for year in year_range:

	print "\n%s stats" % str(year)
	cs229_year = 0
	nips_year = 0

	directory = "../data/text/%s" % str(year)
	files = os.listdir(directory)

	for f in files:

		if f.endswith(".txt"):

			if "cs229" in f:
				cs229 += 1
				cs229_year += 1 

			elif "nips" in f:
				nips += 1
				nips_year += 1

	print "%s cs229 count: %d" % (str(year), cs229_year)
	print "%s nips count: %d" % (str(year), nips_year)
	total_year = cs229_year + nips_year
	print "%s count: %d" % (str(year), total_year)

print "\nTotal stats"
print "total cs229 count: %d" % cs229
print "total nips count: %d" % nips
total = cs229 + nips
print "total count: %d" % total
