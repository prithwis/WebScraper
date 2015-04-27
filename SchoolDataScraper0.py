# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 15:36:32 2015

Extract data on addresses of Schools in Calcuttta and load
into TSV file for subsequent geocoding

@author: Prithwis Mukerjee
"""
import string
import urllib2
from bs4 import BeautifulSoup

f = open('CalcuttaSchools.tsv','w')

url1 = 'http://www.hindustanlink.com/careertex/india_institutes/kolkata-calcutta-schools.htm'
url2 = 'http://www.hindustanlink.com/careertex/india_institutes/kolkata-shools2.htm'
url3 = 'http://www.hindustanlink.com/careertex/india_institutes/kolkata-shools3.htm'

for url in [url1,url2,url3]:
    page = urllib2.urlopen(url)
    soup = BeautifulSoup(page)
    
    table = soup.find('table', attrs={'class': 'MsoTableGrid'})
    rows = table.findAll('tr')
    FirstRow = True
    
    for tr in rows:
        cols = tr.findAll('td')
        if FirstRow:
            FirstRow = False
        else:
            SchoolName = cols[1].text
            SchoolAddr = cols[2].text
            
            SchoolName = filter(lambda x: x in string.printable, SchoolName)
            SchoolName = SchoolName.replace("\n","").rstrip().lstrip()
            SchoolName = ' '.join(SchoolName.split())
            
           
            SchoolAddr = filter(lambda x: x in string.printable, SchoolAddr)
            SchoolAddr = SchoolAddr.replace("\n","").replace(",","").rstrip().lstrip()
            SchoolAddr = SchoolAddr.replace("Calcutta",",Kolkata,India,")
            SchoolAddr = ' '.join(SchoolAddr.split())
            SchoolAddr = SchoolAddr.replace(" ,",",")
            l = len(SchoolAddr)
            PinCode = SchoolAddr[l-8:l].replace(" ","")
            SchoolAddr = SchoolAddr[:-8]+PinCode
            
            f.write(SchoolName+'\t'+SchoolAddr+'\n')
            #print SchoolName+","+SchoolAddr
    

f.close()

"""

Reading HTML table
http://stackoverflow.com/questions/15250455/how-to-parse-html-table-with-python-and-beautifulsoup-and-write-to-csv
Removing non printable characters from string
http://stackoverflow.com/questions/92438/stripping-non-printable-characters-from-a-string-in-python
Replacing multiple blanks with single blank
http://stackoverflow.com/questions/2077897/substitute-multiple-whitespace-with-single-whitespace-in-python
Removing last few characters of string
http://stackoverflow.com/questions/1798465/python-remove-last-3-characters-of-a-string

"""