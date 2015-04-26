# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 08:06:39 2015

retrives list of URLs from the Economic Times website
for company names beginning with 'a'
necessary for next program

@author: prithwis mukerjee
"""

# -*- coding: utf-8 -*-

import urllib2
from bs4 import BeautifulSoup

prefix = "http://economictimes.indiatimes.com"
middle = "/markets/stocks/stock-quotes?ticker="
id = "a"
 
url = prefix+middle+str(id)
page = urllib2.urlopen(url)

soup = BeautifulSoup(page)
xTract1 = soup.find_all(attrs={"class":"companyList"})
soup = BeautifulSoup(str(xTract1[0]))
for link in soup.find_all('a'):
        print prefix+(link.get('href'))
        
