import os
import re
from time import sleep
from urllib2 import urlopen
from bs4 import BeautifulSoup as bs
import requests

num_range = range(18, 26)

for num in num_range:

    sleep(1)
    counter = 0
    year = num + 1987

    print "...getting papers from %s \n" % str(year)

    directory = "../data/pdf/%s" % str(year)
    year_url = "http://books.nips.cc/nips" + str(num) + ".html"    
    data = urlopen(year_url).read()
    soup = bs(data)

    for a in soup.find_all("a"):

        href = a.get("href")

        try:
            if href.endswith('.pdf'):
                if "slide" not in href:

                    name = "nips-%s-%s.pdf" % (year, counter)
                    fullname = "%s/%s" % (directory, name)

                    pdf_url = str(href)
                    r = requests.get(pdf_url)
                    with open(fullname, "wb") as pdf: 
                        pdf.write(r.content)

                    print "...downloading %s as %s" % (href, name)
                    counter += 1

        except:
            pass
