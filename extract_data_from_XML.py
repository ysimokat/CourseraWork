#!/usr/bin/env python2
"""
In this assignment you will write a Python program somewhat similar
to http://www.pythonlearn.com/code/geoxml.py. The program will prompt for 
a URL, read the XML data from that URL using urllib and then extract the 
comment counts from the XML data, compute the sum of the numbers in the file.
-----------------------------------------------------------------
data: http://python-data.dr-chuck.net/comments_298660.xml(sum ends with 11)
"""

import urllib
import xml.etree.ElementTree as ET

#example data
url = "http://python-data.dr-chuck.net/comments_298660.xml"
n = 0
sums = 0
address = urllib.urlopen(url).read()
print "Retrieved: ", len(address), "characters"
tree = ET.fromstring(address)

lst = tree.findall('.//comment') #list
for item in lst:
    count = int(item.find('count').text)
    sums = sums + count
    n = n +1
print "Counts: ", n
print "Sums: ", sums
