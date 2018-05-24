#!/usr/bin/python3

def myrange2(x, y=None, i=None):
    """ Return a list using the user-defined inputs
    """

    y = x+1 if y is None else y
    i = 1 if i is None else i

    ## Sanity checks
    if x > y:
        print("Whoops x({x}) > y({y})")
        exit(1)

    mylist = [x]
    while x < y:
        # iterate x
        x += i
        if x < y:
            mylist.append(x)

    return mylist


## Main
if __name__ == "__main__":
    
    print("using 10, 30, 3 in myrange2")    
    for x in myrange2(10, 30, 3):
        print x
    print myrange2(10, 30, 3)

    print("using 10, 16 in myrange2")
    for x in myrange2(10, 16):
        print x
    print myrange2(10, 16)


    print("using 9 in myrange2")
    for x in myrange2(9):
        print x
    print myrange2(9)
