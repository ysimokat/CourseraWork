#!/usr/bin/env python2
import sqlite3
"""
Counting Organizations
-------------------------
This application will read the mailbox data (mbox.txt) count up the email messages per
organization (i.e. domain name of the email address) using a database with the following 
schema to maintain the counts.

CREATE TABLE Counts (org TEXT, count INTEGER)
"""
#connecting to the file in which we want to store our database
conn = sqlite3.connect('db1.sqlite')
cur = conn.cursor()

#Deleting any possible table that may affect this assignment
cur.execute('''
DROP TABLE IF EXISTS Counts''')

#Creating the table
cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')

#request user input file name
fname = raw_input("Enter file name: ")
fh = open(fname)

#reading each line in this file
for line in fh:
    #Finding an email address and split into name and organization
    if not line.startswith('From: ') : continue
    pieces = line.split()
    org = pieces[1]
    print org
    (email,org) = org.split("@")
    #Updating the table
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (org, )) #single tuple
    row =  cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (org, count) 
                VALUES ( ?, 1)''', ( org, ))
    else: 
        cur.execute('UPDATE Counts SET count=count+1 WHERE org = ?', 
            (org, )) #email-'?'
#This statement commits outstanding changes to disk each
#time through the loop - the program can be made faster
#by moving the commit so it runs only after the loop completes
    conn.commit()

#getting the top 10 results
#http://www.sqlite.org/lang_select.html
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

print
print "Counts: "
for row in cur.execute(sqlstr):
    print str(row[0]), row[1]

#closing the database
cur.close()
