#!/usr/bin/python3
from collections import namedtuple

class GuestList:
    #def __init__(self):
        
    def assign(self, Person):
        print("Person:{}".format(Person))
        

gl = GuestList()
Person = ('Evan',22,'a while ago')
print("Person:{}".format(Person, ))
gl.assign(Person)
