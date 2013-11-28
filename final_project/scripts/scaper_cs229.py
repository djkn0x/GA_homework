"""
This script uses requests and BeautifulSoup to find and download final project papers 
from the Stanford CS229 Machine Learning course. 

"""

import os
import re
from time import sleep
from urllib2 import urlopen
from bs4 import BeautifulSoup as bs
import requests

year_range = range(2005, 2013)

for year in year_range:

    counter = 0
    sleep(1)
    print "...getting projects from %s \n" % str(year)

    directory = "../data/pdf/%s" % str(year)
    year_url = "http://cs229.stanford.edu/projects" + str(year) + ".html"    
    data = urlopen(year_url).read()
    soup = bs(data)

    for a in soup.find_all("a"):

        try:
            if "pdf" in a["href"]:
                href = a.get("href")

                name = "cs229-%s-%s.pdf" % (year, counter)
                fullname = "%s/%s" % (directory, name)

                pdf_url = "http://cs229.stanford.edu/" + str(href)
                r = requests.get(pdf_url)
                with open(fullname, "wb") as pdf: 
                    pdf.write(r.content)

                print "...downloading %s as %s" % (href, name)
                counter += 1

        except:
            pass
