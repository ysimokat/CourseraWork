#!/usr/bin/env python2
import urllib
from bs4 import BeautifulSoup 

count = 0
position = 0

url = "http://python-data.dr-chuck.net/known_by_Keziah.html"
while count<7:
	html = urllib.urlopen(url).read() #read all
	soup = BeautifulSoup(html,"lxml")
    
	#retrieve a list of the anchor tags
	#each tag is like a dictionary of HTML attributes
	
	tags = soup('a') #look tag start with <a>,</a>
	for j in tags:
		position = position + 1
		if position==18:
			url = j.get('href', None)
			print url
			position = 0
			break	
	count = count + 1
