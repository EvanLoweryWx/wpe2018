#!/usr/bin/python3

import hashlib
import os

class DirFileHash(object):

    def __init__(self, dir_cur):
        self.dir_cur = dir_cur

    def __print__(self, fname):
        # get the full file path
        fpath = self.dir_cur + fname
        
        # make sure the file path exists
        if not os.path.isfile(fpath):
            return None

        # find the MD5 hash of the file
        m = hashlib.md5()
        data = None
        with open(fpath) as f:
            data = f.readlines()
        return m.update(data).hexdigest()
    

d = DirFileHash('/etc/')
print(d['passwd'])
