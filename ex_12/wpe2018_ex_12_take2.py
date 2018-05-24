#!/usr/bin/python3

import hashlib
import os

class DirFileHash(object):
    
    def __init__(self, dirname):
        self.dirname = dirname

    def __getitem__(self, filename):
        
        ## get the full filepath
        filepath = os.path.join(self.dirname, filename)
    
        ## Make sure filepath exists
        if not os.path.exists(filepath) or not os.path.isfile(filepath):
            return None, None

        ## get the md5 (full slurp)
        m = hashlib.md5()
        m.update(open(filepath, 'rb').read())
        hex1 = m.hexdigest

        ## line by line
        blocksize = 2**20
        n = hashlib.md5()
        with open(filepath, 'rb') as f:
            while True:
                buf = f.read(blocksize)
                if not buf:
                    break
                n.update
            
        hex2 = m.hexdigest

        return hex1, hex2

d = DirFileHash('/etc/')
print(d['passwd'])            
