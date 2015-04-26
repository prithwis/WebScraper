# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 08:27:14 2015

Gets company financial data from the Economic Times Website
for a range of companies whose URLs have been extracted by GetURLLinks program
and stored in a text file.

Writes the data into a another textfile

@author: hduser
"""

import urllib2
from bs4 import BeautifulSoup

f = open('GetCompanyDataOutput.csv','w')
f.write("Comp,Sales,OthOpInc,OpProfit,EBITDA,Interest,Dep,Tax,NetP,EPS"+"\n")

URLfile = open('GetURLLinksOutput-extract.txt', 'r')
for URL in URLfile:
    print URL
    page = urllib2.urlopen(URL)
    soup = BeautifulSoup(page)
    
    spoon1 = soup.find_all(attrs={"class":"flt quartYear bold w132"})
    
    
    Sales = spoon1[0].span.string.replace(",","")
    OthOpInc = spoon1[1].span.string.replace(",","")
    OpProfit = spoon1[2].span.string.replace(",","")
    OpInc = spoon1[3].span.string.replace(",","")
    EBITDA = spoon1[4].span.string.replace(",","")
    Interest = spoon1[5].span.string.replace(",","")
    Dep = spoon1[6].span.string.replace(",","")
    Tax = spoon1[7].span.string.replace(",","")
    NetP = spoon1[8].span.string.replace(",","")
    EPS = spoon1[9].span.string.replace(",","")
    
    #Comp = spoon2[0].span.string
    #print(Sales,OthOpInc,OpProfit, OpInc,EBITDA,Interest,Dep,Tax,NetP,EPS)
    
    title1 = soup.title.string
    Com = title1[:(title1.find("Share")-1)]
    Com = Com.rstrip()
    
    f.write(Com+","+Sales+","+OthOpInc+","+OpProfit+","+EBITDA+","+Interest+","+Dep+","+Tax+","+NetP+","+EPS+"\n")
    
  
    
f.close()
URLfile.close()
