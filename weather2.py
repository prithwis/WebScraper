# -*- coding: utf-8 -*-

import urllib2
from bs4 import BeautifulSoup
f = open('wunder-data.txt','w')
url1 = "http://www.wunderground.com/history/airport/VECC/"
url2 = "/DailyHistory.html"

for y in range(2001,2004):
    for m in range(1,4):
        for d in [1,8,15]:
            
            if (m == 2 and d > 28):
                break
            elif(m in [4,6,9,11] and d > 30):
                break
            
            
            if len(str(m))<2:
                mStamp = "0"+str(m)
            else: mStamp = str(m)
            if len(str(d)) < 2:
                dStamp = "0"+str(d)
            else: dStamp = str(d)
            
            timestamp = str(y)+mStamp+dStamp
            print "getting data for: " + timestamp
            url = url1+ str(y) + "/" + str(m) + "/" + str(d) + url2
            print url
            page = urllib2.urlopen(url)
            soup = BeautifulSoup(page)
            wxdatas = soup.findAll(attrs={"class":"wx-data"})
            
            dayMaxTemp = wxdatas[1].span.string
            dayMinTemp = wxdatas[4].span.string
            print dayMaxTemp, dayMinTemp
            
            f.write(timestamp+":"+dayMaxTemp+":"+dayMinTemp+'\n')
        
f.close()