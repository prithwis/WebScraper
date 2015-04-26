# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 08:24:52 2015

Getting company financial data from Economic Times website from
the page of one specific company

@author: Prithwis Mukerjee
"""

import urllib2
#page = urllib2.urlopen("http://economictimes.indiatimes.com/ludlow-jute-and-specialities-ltd/stocks/companyid-9874.cms")
page = urllib2.urlopen("http://economictimes.indiatimes.com/bajaj-auto-ltd/stocks/companyid-21430.cms")
from bs4 import BeautifulSoup
soup = BeautifulSoup(page)
xTract1 = soup.findAll(attrs={"class":"flt quartYear bold w132"})

print xTract1[0].span.string
print xTract1[1].span.string
print xTract1[2].span.string
print xTract1[3].span.string
print xTract1[4].span.string
print xTract1[5].span.string
print xTract1[6].span.string
print xTract1[7].span.string
print xTract1[8].span.string
print xTract1[9].span.string
