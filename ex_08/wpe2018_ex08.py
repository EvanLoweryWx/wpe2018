#!/usr/bin/python3

import os
from pprint import pformat

def evanfunc(dir_in, func_in):
    """ Ingest a directory and user-defined function
        List all the files in the directory and run them through the user-defined
        function
    """
   
    ## make sure directory exists
    if not os.path.exists(dir_in):
        print("psst, dir_in({0}) does not exist".format(dir_in, ))
        exit(1)
 
    ## change directory
    os.chdir(dir_in)
    print("Currently in dir:{0}".format(dir_in, ))

    ## get a list of file names in directory
    #fnames = os.listdir(dir_in)
    #print("Files:{0}".format(pformat(fnames)))

    ## loop through files
    results, exceptions = {}, {}
    for fname in os.listdir(dir_in):
        result, exception = func_in(fname)
        #print("fname({0}), results({1}), exception({2})".format(fname, result, exception))
        if result is not None:
            results[fname] = result
        if exception is not None:
            exceptions[fname] = exception
    
    return results, exceptions


def file_length(filename):

    try:
        return os.stat(filename).st_size, None
    except Exception as e:
        return None, e

dir_test = '/etc/'
success_dict, failure_dict = evanfunc(dir_test, file_length)

print("Examined dir:{0}".format(dir_test, ))
print("Success_dict:{0}".format(pformat(success_dict, )))
print("Failure_dict:{0}".format(pformat(failure_dict, )))
