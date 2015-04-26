# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 08:14:03 2015

Extension of GetURLLinks0 --
iteratively gets URLs from a series of pages to get data
on companies with names starting with a,b,c 
write the data into a file to be used by subsequent program

@author: Prithwis Mukerjee
"""

import urllib2
from bs4 import BeautifulSoup
f = open('GetURLLinksOutput.txt','w')
prefix = "http://economictimes.indiatimes.com"
middle = "/markets/stocks/stock-quotes?ticker="
#
# we are picking only id = a,b,c here
# see http://stackoverflow.com/questions/16060899/alphabet-range-python
#
for id in map(chr, range(97, 100)):  
    url = prefix+middle+str(id)
    page = urllib2.urlopen(url)

    soup = BeautifulSoup(page)
    xTract1 = soup.find_all(attrs={"class":"companyList"})
    soup = BeautifulSoup(str(xTract1[0]))
    for link in soup.find_all('a'):
        #print prefix+(link.get('href'))
        f.write(prefix+(link.get('href'))+'\n')
        
f.close()