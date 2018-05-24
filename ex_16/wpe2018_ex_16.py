#!/usr/bin/python3

class ThresholdEqual(object):

    def __init__(self, x, tolerance=2):
        self.x = x
        self.tolerance = tolerance
        print("x({0}), tolerance({1})".format(self.x, self.tolerance, ))
        
    def __eq__(self, other):
        if abs(self.x - other.x) <= self.tolerance:
            return True
        else:
            return False


ex1 = ThresholdEqual(7, 1)
ex2 = ThresholdEqual(5, 1)
print(ex1 == ex2)
