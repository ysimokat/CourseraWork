#!/usr/bin/env python2

"""
In this assignment you will write a Python program somewhat similar to 
http://www.pythonlearn.com/code/geojson.py

The program will prompt for a location, contact a web service and 
retireve JSON for the web service and parse that data, and retrieve the first 
place_id from the JSON. A place ID is a textual identifier that uniquely identifies
a place as within Google Maps.

API End Points
--------------
To complete this assignment, you should use this API endpoint that has a static subset
of the Google Data: http://python-data.dr-chuck.net/geojson?

This API uses the same parameters(sensor and address) as the Google API. This API
also has no rate limit so you can test as often as you like. If you visit the URL with 
ChIJJ8oO7_B_bIcR2AlhC8nKlok
no parameters,you get a list of all of the address values which can be used with this 
API.

To call the API, you need to provide a sensor=false parameter and the address that you 
are requesting as the address= parameter that is properly URL encoded using the
urllib.urlencode() function as shown in http://www.pythonlearn.com/code/geojson.py

Test Data/Sample Execution
--------------------------
You can test to see if your program is working with a location of "South Federal University"
which will have a place_id of "ChIJJ8oO7_B_bIcR2AlhC8nKlok".
"""

import urllib
import json

serviceurl =  'http://python-data.dr-chuck.net/geojson?'

while True:
    address = raw_input('Enter location: ')
    if len(address) < 1 : break

    url = serviceurl + urllib.urlencode({'sensor':'false', 'address': address})
    print 'Retrieved', url

    data = urllib.urlopen(url).read()
    print 'Retrieved', len(data), 'Characters'

    try: js = json.loads(str(data))
    except: js = None
    if 'status' not in js or js['status'] != 'OK':
        print '==== Failure To Retrieve ===='
        print data
        continue
    
    #print json.dumps(js, indent=4)

    place_ID =  js["results"][0]["place_id"]   
    print "Place id: ", place_ID




#University of Dallas 
#Place id: ChIJJQoISt9C6oYRfYtBguvi5c0





