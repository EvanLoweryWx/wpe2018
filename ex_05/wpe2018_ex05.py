#!/usr/bin/python3

## import modules
import csv
import json
import os
import urllib.request
from pprint import pprint

## Download raw json
json_csv = "cities.csv"
json_fname = "cities.json"
json_link = "https://gist.githubusercontent.com/reuven/77edbb0292901f35019f17edb9794358/raw/2bf258763cdddd704f8ffd3ea9a3e81d25e2c6f6/{}".format(json_fname, )
#print("json_fname({}), json_link({})".format(json_fname, json_link, ))

# remove file if exists
if os.path.isfile(json_fname):
    os.remove(json_fname)

# download file
urllib.request.urlretrieve(json_link, json_fname)

# did we successfully download file?
if not os.path.isfile(json_fname):
    print("Well shit, json_fname({}) was not downloaded".format(json_fname, ))
    exit(1)

## Ingest data via json module
data = json.load(open(json_fname))
#pprint(data[0])

## Dump files to a csv file using the csv module

# remove file if exists
if os.path.isfile(json_csv):
    os.remove(json_csv)

# misc
delim = "\t"
new_line = "\n"

# headers
headers = ["City name","State name","City population","City size rank",]

with open(json_csv, 'w') as f:
    fline = ""
    for cur_header in headers:
        fline += cur_header + delim

    fline += new_line
    f.write(fline)

    for cur_data in data:
        fline = cur_data['city'] + delim
        fline += cur_data['state'] + delim
        fline += cur_data['population'] + delim
        fline += cur_data['rank'] + new_line
        f.write(fline)
