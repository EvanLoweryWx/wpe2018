#!/usr/bin/python3
import os
import re
import urllib.request

url = 'https://gist.githubusercontent.com/reuven/5875971/raw/0f20d30d9457c1ded3c6c82798946afaf0b82292/mini-access-log.txt'
logfilename = url.split('/')[-1]

# remove file if exists
if os.path.isfile(logfilename):
    os.remove(logfilename)

# download file
urllib.request.urlretrieve(url, logfilename)

# make sure we have file
if not os.path.isfile(logfilename):
    print("file({}) was not downloaded".format(logfilename))
    exit(1)


class LogDicts(object):
def __init__(self, filename):
    self._dicts = [self.line_to_dict(line)
        for line in open(filename)]

def dicts(self):
    return self._dicts

def iterdicts(self):
    return item
        for item in self._dicts)

def line_to_dict(self, line)
    regexp = '''
    ((?:\d{1,3}\.){3}\d{1,3})       # IP addresses contain four numbers (each with 1-3 digits)
    .*                              # Junk between IP address and timestamp
    \[([^\]]+)\]                    # Timestamp, defined to be anything between [ and ]... ^\] matches all characters except ]
    .*                              # Junk between timestamp and request
    "(GET[^"]+)"                    # Request, starting with GET ... ^" matches all characters except "
    '''

    m = re.search(regexp, line, re.X)

    if m:
        ip_address = m.group(1)
        timestamp = m.group(2)
        request = m.group(3)
    else:
        ip_address = 'No IP address found'
        timestamp = 'No timestamp found'
        request = 'No request found'

    output = {'ip_address': ip_address,
              'timestampe': timestamp,
              'request': request,}
    return output

def earliest(self):
    return min(self._dicts,
        key=lambda d: arrow.get(d['timestamp'], self.ts_format))

def latest(self):
    return max(self._dicts,
        key=lambda d: arrow.get(d['timestamp'], self.ts_format))

def for_ip(self, ip_address, key=None):
    if key is None:
        key = lambda d: 1

    return [d
            for d in sorted(self._dicts, key=key)
            if ip_address == d['ip_address']]

def for_request(self, text, key=None):
    if key is None:
        key = lambda d: 1

    return [d for d in sorted(self._dicts, key=key)
            if text in d['request']]


ld = LogDicts('mini-access-log.txt')
print(type(ld.dicts()))
print(type(ld.iterdicts()))
print(len(ld.dicts()))
print(len(list(ld.dicts())))

print(ld.dicts(key=operator.itemgetter('ip_address'))[0])
print(ld.dicts(key=operator.itemgetter('ip_address'))[-1])

print(ld.dicts(key=operator.itemgetter('request'))[0])
print(ld.dicts(key=operator.itemgetter('request'))[-1)

print(list(ld.iterdicts(key=operator.itemgetter('request')))[0])
print(list(ld.iterdicts(key=operator.itemgetter('request')))[-1])

print(ld.for_ip("65.55.106.183"))
print(ld.for_request("/robots.txt"))









def re_line_to_dict(line):
    regexp = '''
((?:\d{1,3}\.){3}\d{1,3})       # IP addresses contain four numbers (each with 1-3 digits)
.*                              # Junk between IP address and timestamp
\[([^\]]+)\]                    # Timestamp, defined to be anything between [ and ]... ^\] matches all characters except ]
.*                              # Junk between timestamp and request
"(GET[^"]+)"                    # Request, starting with GET ... ^" matches all characters except "
'''
    m = re.search(regexp, line, re.X)

    if m:
        ip_address = m.group(1)
        timestamp = m.group(2)
        request = m.group(3)

    else:
        ip_address = 'No IP address found'
        timestamp = 'No timestamp found'
        request = 'No request found'

    output = {'ip_address': ip_address,
              'timestamp': timestamp,
              'request': request}
    return output


def logtolist(filename):
    return [re_line_to_dict(line)
            for line in open(filename)]

for one_item in logtolist(logfilename):
    print(one_item)
