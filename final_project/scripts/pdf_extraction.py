from time import sleep
import os
import pdfminer

year_range = range(2006, 2013)

for year in year_range:

	sleep(1)
	print "\n...starting %s files" % str(year)

	directory = "../data/pdf/%s" % str(year)
	files = os.listdir(directory)

	for f in files:

		input_file = '"' + "../data/pdf/%s/%s" % (str(year), f) + '"'

		output = os.path.splitext(os.path.basename(f))[0] + ".txt"
		output_file = "../data/text/%s/%s" % (str(year), output)

		if ".pdf" in input_file:
			print "...extracting %s as %s" % (input_file, output_file)
			try:
				os_call = str("pdf2txt.py -c utf-8 -o %s %s" % (output_file, input_file)) 
				os.system(os_call)
			except: 
				pass
