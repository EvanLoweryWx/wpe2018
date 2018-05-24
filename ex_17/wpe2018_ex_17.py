#!/usr/bin/python3

''' Magic tuples
'''

def magic_tuples(total, max_val):
    '''
    total:      total of two tuple elements
    max_val:    maximum value of an element -1'''

    x, y = 1, (max_val-1)
    #print("Current x({0}), y({1})".format(x, y))
    #exit(0)
    while x < max_val:
        if (x+y) == total:
            yield (x, y)
            x += 1
            y = max_val-1
        elif y == 1:
            x += 1
            y = max_val-1
        else:
            y -= 1

print("Trying 5,4")
for t in magic_tuples(5,4):
    print(t)

print("Trying 10,20")
for t in magic_tuples(10,20):
    print(t)
