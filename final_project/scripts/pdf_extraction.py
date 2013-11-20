from time import sleep
import os
import pdfminer

for a in range(2012,2013):

	sleep(1)
	print "\n...starting %s files" % str(a)

	directory = "../data/pdf/%s" % str(a)
	files = os.listdir(directory)

	for f in files:

		input_file = '"' + "data/pdf/%s/%s" % (str(a), f) + '"'

		output = os.path.splitext(os.path.basename(f))[0] + ".txt"
		output_file = "data/text/%s/%s" % (str(a), output)

		if ".pdf" in input_file:
			try:
				os_call = str("pdf2txt.py -o %s %s" % (output_file, input_file)) 
				os.system(os_call)
			except: 
				pass
