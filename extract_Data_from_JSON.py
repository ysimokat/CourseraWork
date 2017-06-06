#!/usr/bin/env python2
"""
In this assignment you will write a Python program somewhat similar to 
http://www.pythonlearn.com/code/json2.py
The program will prompt for a URL,read the JSON data from that URL using 
urllib and then parse and extract the comment counts from the JSON data,
compute the sum of the numbers in the file and enter the sum below:

Actual Data: http://python-data.dr-chuck.net/comments_298664.json
(sum ends with 28)
"""

import urllib
import json

n = 0
sums = 0
#url = "http://python-data.dr-chuck.net/comments_42.json" #sum=2553
while True:
    url = raw_input("Enter location: ")
    if len(url) < 1: break 

    print "Retrieving", url
   
    connection =  urllib.urlopen(url)
    data =  connection.read() #body json
    print "Retrieving", len(data), "Characters"

    js = json.loads(data)
    #print json.dumps(js, indent=4) #json pretty print
    
    for u in js['comments']:
        n = n + 1
        sums = sums + u['count']
    print "Count: ", n
    print "Sum: ", sums
    break
