import os
import re
from time import sleep
from urllib2 import urlopen
from bs4 import BeautifulSoup as bs
import requests

for a in range(2005,2013):
    print "...getting projects from %s \n" % str(a)

    directory = "../data/%s" % str(a)

    year_url = "http://cs229.stanford.edu/projects" + str(a) + ".html"    
    data = urlopen(year_url).read()
    soup = bs(data)

    for a in soup.find_all("a"):
        try:
            if "pdf" in a["href"]:
                sleep(0.2)
                href = a.get("href")
                
                name = re.sub("http://cs229.stanford.edu/proj", "", href)
                filename = re.sub("/", "-", name)  # to strip "/" character from filename
                fullname = "%s/%s" % (directory, filename)

                pdf_url = "http://cs229.stanford.edu/" + str(href)
                r = requests.get(pdf_url)
                with open(fullname, "wb") as pdf: 
                    pdf.write(r.content)

        except:
            pass
