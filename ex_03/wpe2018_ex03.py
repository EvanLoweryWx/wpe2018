#!/usr/bin/python3
import os
import re
import urllib.request

url = 'https://gist.githubusercontent.com/reuven/5875971/raw/0f20d30d9457c1ded3c6c82798946afaf0b82292/mini-access-log.txt'
file_name = url.split('/')[-1]

# remove file if exists
if os.path.isfile(file_name):
    os.remove(file_name)

# download file
urllib.request.urlretrieve(url, file_name)

# make sure we have file
if not os.path.isfile(file_name):
    print("file({}) was not downloaded".format(file_name))
    exit(1)

# initialize stuff
dict_list = []
log_pattern = re.compile(r"^(.+)\s\-\s\-\s\[(.+)\]\s\"(.+)\"\s")

# open file
with open(file_name) as f:
    for line in f:
        # use re to find ip_address, timestamp, request
        #
        #67.218.116.165 - - [30/Jan/2010:00:03:18 +0200] "GET /robots.txt HTTP/1.0" 200 99 "-" "Mozilla/5.0 (Twiceler-0.9 http://www.cuil.com/twiceler/robot.html)"
        
        # Does the current line match the log_pattern?
        m = re.search(log_pattern, line)
        if m:
            dict_list.append([{
                'ip_address': m.groups()[0],
                'timestamp': m.groups()[1],
                'request': m.groups()[2],
            }])
            print("line({})".format(line))
            print("m({})".format(m.groups()))
            print(dict_list[0])
            exit(1)
        else:
            print("line({}) does not match log_pattern".format(line))
            exit(1)

for cur_dict in dict_list:
    print(cur_dict)
    exit(1)
    #[{
    #'ip_address': '67.218.116.165', 
    #'timestamp': '30/Jan/2010:00:03:18 +0200', 
    #'request': 'GET /robots.txt HTTP/1.0" 200 99 "-" "Mozilla/5.0 (Twiceler-0.9 http://www.cuil.com/twiceler/robot.html)'}]
