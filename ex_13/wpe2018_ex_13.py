#!/usr/bin/python3

import random
#print(random.randint(1,100))a

class RandMemory(object):
    
    def __init__(self, randMin, randMax):
        self.randMin = randMin
        self.randMax = randMax
        self.randHist = []

    def get(self):
        randInt = random.randint(self.randMin, self.randMax)
        self.randHist.append(randInt)
        return randInt

    def history(self):
        return self.randHist


r = RandMemory(1,100)
r.get()
r.get()
r.get()
print(r.history())
