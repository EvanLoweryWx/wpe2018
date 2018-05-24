#!/usr/bin/python3

## https://www.learnpython.org/en/Classes_and_Objects


class Vehicle:
    """ Vehicle Class
    """
    name = ""
    kind = "car"
    color = ""
    value = 100.00
    
    def description(self):
        #desc_str = "{} is a {} {} worth {}".format(self.name, self.color, self.kind, self.value, )
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value, )
        return desc_str

    def description2(self):
        self.value **= 2
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value, )
        return desc_str



class MyClass:
    variable = "blah"

    def function(self):
        print("This is a message inside the class.")


car1 = Vehicle()
car2 = Vehicle()

car1.name = "Fer"
car1.color = "red"
car1.value = 60000

car2.name = "Jump"
car2.color = "blue"
car2.value = 10000

print(car1.description())
print(car2.description())

print(car1.description2())
print(car2.description2())




exit(0)

myObj1 = MyClass()
myObj2 = MyClass()

myObj1.variable = "poop"

print(myObj1.variable)
print(myObj2.variable)
myObj1.function()
