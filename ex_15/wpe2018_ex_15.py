#!/usr/bin/env python3

import glob
import os
import threading
import time
from queue import Queue

def count_words(files):
    
    wordcount = 0
    for cur_file in glob.glob(files):
        ## open the file and count words
        print("Cur file:{0}".format(cur_file))
        f = open(cur_file, 'r')
        for word in f.read().split():
            wordcount += 1
        
        f.close()

        print("{0} words found in cur file:{1}".format(wordcount_cur, cur_file))
    
    

files = '/home/evan/sandbox/reuven_2018/ex_15/gutenberg_books/*.txt'

ts_beg = time.time()
count_words(files)
ts_diff = time.time() - ts_beg
print("count_words run sequentially in {0} seconds".format(ts_dif))


## Start a queue
q = Queue()

ts_beg = time.time()
t = {}
i = 0
for cur_file in glob.glob(files):
    i += 1
    t[i] = Thread(target=count_words_threading, args=(cur_file,)
    t[i].start()

for j in range(1, i+1, 1):
    t[j].join()

ts_diff = time.time() - ts_beg
print("count_words run threads in {0} seconds".format(ts_diff))
