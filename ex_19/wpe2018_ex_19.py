#!/usr/bin/python3

import string

''' Ex 19: Password checker
'''

def create_password_checker(min_uc, min_lc, min_punc, min_digits):
    ''' This function returns a function which can be used to check passwords
        based on the user specified inputs of this fx
    '''

    def check_the_password(user_pw):
        num_uc = sum(1 for c in user_pw if c.isupper())
        num_lc = sum(1 for c in user_pw if c.islower())
        num_punc = sum(1 for c in user_pw if c in string.punctuation)
        num_digits = sum(1 for c in user_pw if c.isdigit())

        pass_tests = True
        if num_uc < min_uc:
            pass_tests = False
        if num_lc < min_lc:
            pass_tests = False
        if num_punc < min_punc:
            pass_tests = False
        if num_digits < min_digits:
            pass_tests = False

        return(
            pass_tests,
            {'uppercase': (num_uc - min_uc),
             'lowercase': (num_lc - min_lc),
             'punctuation': (num_punc - min_punc),
             'digits': (num_digits - min_digits),
            }
        )

    return check_the_password


pc = create_password_checker(1, 3, 5, 7)
print(pc('evanLowery3$$56')) #False
print(pc('evanLowery3$!:<>1367378')) #True
print(pc('evanLowery3$!:<>13673')) #False
