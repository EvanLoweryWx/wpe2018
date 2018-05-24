#!/usr/bin/python3

def multiziperator(str1, list1, str2):
    idx = 0
    
    ## Find min len
    min_len = 999999 #absurdly large number
    if len(str1) < min_len:
        min_len = len(str1)
    if len(list1) < min_len:
        min_len = len(list1)
    if len(str2) < min_len:
        min_len = len(str2)

    while idx < min_len:
        yield str1[idx]
        yield list1[idx]
        yield str2[idx]
        idx += 1


letters = 'abcde'
numbers = [1,2,3,4,5]
symbols = '^@$'

for item1 in multiziperator(letters, numbers, symbols):
    print(item1)
