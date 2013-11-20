import os

combined = []

for a in range(2005,2013):

	directory = "../data/text/%s" % str(a)
	files = os.listdir(directory)

	for f in files:

		if ".txt" in f:
			try:

				filename = directory + "/" + f
				text = open(filename).read().lower()
				combined.append(text)

			except:
				pass

f = open("../data/text/fulltext.txt", 'w')
f.write(str(combined))
f.close()
