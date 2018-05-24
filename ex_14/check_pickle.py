#!/bin/env python
""" maintain an address book.
"""
import os
import time
import pickle

menu = """
a: Add Person
l: List People
r: Restore via timestamp
q: Quit program
"""

addr_book = []
save_dir = 'backup'
if not os.path.isdir(save_dir):
    os.makedirs(save_dir)


while True:
    print(menu)
    choice = input('?> ')
    if choice.lower() == 'q':
        break

    elif choice.lower() == 'l':
        for person in addr_book:
            print('{last}, {first}......{email}'.format(**person))

    elif choice.lower() == 'a':
        print('Add new person: ')
        first = input('First name: ')
        last = input('Last name: ')
        email = input('E-mail: ')
        addr_book.append({'first': first, 'last': last, 'email': email})
        save_file = '%s/addr_book_%d.pkl' % (save_dir, time.time())
        with open(save_file, 'wb') as fp:
            pickle.dump(addr_book, fp)

    elif choice.lower() == 'r':
        print('Restore from timestamp')
        user_ts = input('Timestamp to restore: ')
        restore_file = '%s/addr_book_%s.pkl' % (save_dir, user_ts, )
        if not os.path.isfile(restore_file):
            print('Restore file does not exist.')
            continue

        with open(restore_file, 'rb') as fp:
            addr_book = pickle.load(fp)
