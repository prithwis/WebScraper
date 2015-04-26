# -*- coding: utf-8 -*-

import urllib2
page = urllib2.urlopen("http://www.wunderground.com/history/airport/VECC/2010/1/1/DailyHistory.html")
from bs4 import BeautifulSoup
soup = BeautifulSoup(page)
wxdatas = soup.findAll(attrs={"class":"wx-data"})
print wxdatas[1]
dayMaxTemp = wxdatas[1].span.string
dayMinTemp = wxdatas[4].span.string
print dayMaxTemp, dayMinTemp