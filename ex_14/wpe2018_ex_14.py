#!/usr/bin/python3

import calendar
import os
import pickle
import time

from pprint import pformat

class addressBook(object):
   
    pickle_dir = "/tmp"
    pickle_stem = "ilovepickles"
 
    def __init__(self):
        self.addresses = []
        self.pickleFiles = []
        self.pickleTS = []


    def askUser(self):
        
        ## Give the user a list of commands
        print("Available commands:")
        print("q: Quit from the program")
        print("l: List all people in the address book")
        print("a: Add a new person to the address book")
        print("r: Restore the address book to the state from a specific timestamp")
    
        ## Keep asking for a command until a user selects q    
        need_cmds = True
        while need_cmds:
    
            ## Make sure we get a valid command
            valid_cmds = ('q','l','a','r')
            while True:
                cmd = input("\nEnter a command(q,l,a,r):")
                if cmd in valid_cmds:
                    break
                else:
                    print("({0}) is not a valid command!".format(cmd))

            ## Execute user command
            if cmd == "q":
                # Quit from the program
                print("Thanks for joining us today, goodbye!")
                return
            
            elif cmd == "l":
                # List all people in the address book
                self.printAddressBook()
                print("Successfully listed the addressbook!")
                
            elif cmd == "a":
                # Add a new person to the address book

                ## Ask three pieces of info (first name, last name, email address)
                self.addAddressBook()
                print("Successfully added an entry to the addressbook!")
            
            elif cmd == "r":
                # Restore the address book to the state from a specific timestamp
                self.restoreAddressBook()
                print("Successfully restored the addressbook!")


    def addAddressBook(self):
    
        ## Ask the user to enter info into the address book    
        print("Enter First Name, Last Name, and Email Address")
        first_name = input("First Name:")
        last_name = input("Last Name:")
        email = input("Email:")
        
        ## Add to the address book
        self.addresses.append({
            'first': first_name,
            'last': last_name,
            'email': email,
        })
        #print("addresses:{0}".format(pformat(self.addresses)))

        ## dump to a pickle file 
        ts = calendar.timegm(time.gmtime())
        pickle_fname = "{0}_{1}.p".format(self.pickle_stem, ts)
        pickle_fpath = os.path.join(self.pickle_dir, pickle_fname)
        pickle.dump( self.addresses, open( pickle_fpath, "wb" ) )

        ## make sure the pickle file was created
        if not os.path.exists(pickle_fpath) or not os.path.isfile(pickle_fpath):
            print("Error: pickle_fpath({0}) was not successfully created".format(pickle_fpath))
            return

        ## Add pickle file to list
        self.pickleFiles.append(pickle_fpath)
        self.pickleTS.append(ts)


    def printAddressBook(self):
        
        ## Print out the address book
        if len(self.addresses) == 0:
            print("No entries in the address book yet!")
            return
        
        print("Listing all people in the address book")
        print("First Name, Last Name, Email Address")
        for address in self.addresses:
            entry = []
            for key, value in address.items():
                entry.append(value)
            print(",".join(entry))
        print("\n")
                            
        return


    def restoreAddressBook(self):

        ## As the user for a timestmap
        print("Enter a timestamp (TS) to restore, valid TS:")
        for ts in self.pickleTS:
            print("TS: {0}".format(ts))
        user_ts = int(input("Enter TS:"))

        if user_ts not in self.pickleTS:
            print("User-defined TS({0}) is not valid, address book will not be restored!".format(user_ts))
            return

        print("Restoring Address book to user-defined TS({0})".format(user_ts))
        pickle_fname = "{0}_{1}.p".format(self.pickle_stem, user_ts)
        pickle_fpath = os.path.join(self.pickle_dir, pickle_fname)
        self.addresses = pickle.load( open( pickle_fpath, "rb" ) )

        return


ab = addressBook()
ab.askUser()
