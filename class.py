#!/usr/bin/env python2
"""
In object oriented programming, a constructor in a class is a special 
block of statements called when an object is created.

Constructors can have additional parameters. These can be used to set
up instance variables for the instance variables for the particular intance
of the class(i.e.,for the particular object).
"""

class PartyAnimal:
    x = 0
    name = ""
    def __init__(self, nam):    #def __init__ #constructor
                    #parameters(nam)
        self.name = nam   #self.name # instance variable
        print self.name, "constructed"
    
    def party(self):
        self.x = self.x + 1
        print self.name, "party count", self.x
"""        
s = PartyAnimal("Sally")
s.party()

j = PartyAnimal("Jim")
j.party()
s.party()
"""

class FootballFan(PartyAnimal):
    """ FootballFan is a class which extends PartyAnimal.
        it has all the capabilities of PartyAnimal and more.
    """
    points = 0 
    def touchdown(self):
        self.points = self.points + 7
        self.party()
        print self.name, "points", self.points

s = PartyAnimal("Sally")
s.party()

j = FootballFan("Jim")
j.party()
j.touchdown()


#'self' is a formal argument that refers to the object itself.
#self.x is saying "x within self"
#self is "global within this object"

#dir() command lists capabilities
#dir() it shows methods and attributies 

#The primary purpose of the constructor is to set up some instance-
#-variables to have the proper initial values when the object is created.

an = PartyAnimal("Wookie")  
#'__init__' an object is created
an.party()
an.party()





