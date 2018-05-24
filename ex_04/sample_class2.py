#!/usr/bin/python3
## https://en.wikibooks.org/wiki/A_Beginner%27s_Python_Tutorial/Classes

class Shape:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.description = "This shape has not yet been described yet"
        self.author = "Nobody has claimed to make this shape yet"

    def area(self):
        return self.x * self.y

    def perimeter(self):
        return 2 * self.x + 2 * self.y

    def describe(self, text):
        self.description = text

    def authorName(self, text):
        self.author = text

    def scaleSize(self, scale):
        self.x = self.x * scale
        self.y = self.y * scale


shape1 = Shape(4, 10)
desc = "This shape is a rectangle"
author = "Evan"
shape1.describe(desc)
shape1.authorName(author)
print("The dimensions of my shape are x({}) by y({})".format(shape1.x, shape1.y, ))
print("The area of my shape is {}".format(shape1.area(), ))
print("The perimeter is {}".format(shape1.perimeter(), ))
print("Description: {}".format(shape1.description, ))
print("Author: {}".format(shape1.author, ))
shape1.scaleSize(10)
print("After scaling by 10, the perimeter is {}".format(shape1.perimeter(), ))

""" How could a class be used wiht Meteorological data?
    - Let's say you have a list of 1000 locations and you need to store the location info associated iwth each one
        loc_info[locationID] = storeLocInfo(db_data)
    - You pull in a bunch of Meteorological data and need to calculate a bunch of derived values using that data
        wx_vals = calcWxData(db_data)

"""
