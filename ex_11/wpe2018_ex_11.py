#!/usr/bin/python3

import sys

#print('Hello', 'world', sys.stdout.write)
#sys.stdout.write('Hello world\n')

class Tee(object):
    
    def __init__(self, *args):
        self._fhs = args
        #for cur_file in self._files:
        #    print("cur_file:{0}".format(cur_file))

    def write(self, text):
        for cur_fh in self._fhs:
            cur_fh.write(text)

f1 = open('/tmp/tee1.txt', 'w')
f2 = open('/tmp/tee2.txt', 'w')
t = Tee(sys.stdout, f1, f2)

t.write('abc\n')
t.write('def\n')
t.write('ghi\n')

f1.close()
f2.close()
