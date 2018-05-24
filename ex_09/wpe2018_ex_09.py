#!/usr/bin/python3
import os
import random
import re

def createMathProblems(num_probs):
    """ create user-defined number of math problems
    """
    
    ## Name math problems file, remove if already exists
    fname_probs = "math_problems_{0}.txt".format(num_probs)
    if os.path.isfile(fname_probs):
        os.remove(fname_probs)

    ## Create the Math problems file
    with open(fname_probs, 'w') as fp:

        fp.write("Answer each of these Math Problems as quickly as possible\n")
        fp.write("\n")

        for i in range(1, num_probs+1, 1):
            ## get two random numbers between 1 and 100
            rand1 = random.randint(1,100)
            rand2 = random.randint(1,100)

            ## determine + or - based on rand1
            problem = '{0}.\t'.format(i)
            if rand1 > rand2:
                problem += '{0} - {1} ='.format(rand1, rand2)
            else:
                problem += '{0} + {1} ='.format(rand1, rand2)

            fp.write('{0}\n'.format(problem))

    return fname_probs


def createAnswerKey(fname_probs, num_probs):
    """ create answer key for math problems in file
    """
    
    ## Make sure Math problems file exists
    if not os.path.isfile(fname_probs):
        print("file({0}) does not exist, exiting!".format(fname_probs))
        exit(1)

    ## Name the Math problems key file, remove if already exists
    fname_key = "math_key_{0}.txt".format(num_probs)
    if os.path.isfile(fname_key):
        os.remove(fname_key)

    ## Create the Math key file
    fkey = open(fname_key, 'w')
    fkey.write("The answers to the math problems can be found below\n")
    fkey.write("\n")

    header_rows = 2

    ## Read in the math problems file
    with open(fname_probs, 'r') as fmath:
        
        i = 0
        for line in fmath:
            i += 1
            ## Header?
            if i <= header_rows:
                # Yes, skip
                continue

            ## Read in line
            m = re.match("^(\d+)\.\t(\d+)\s([\+\-])\s(\d+)\s\=$", line)
            if m is None:
                print("Error matching line({0}), exiting".format(line))
                exit(1)

            prob_num = m.groups()[0]
            num1 = int(m.groups()[1])
            operator = m.groups()[2]
            num2 = int(m.groups()[3])

            #print("prob_num({0}), num1({1}), operator({2}), num2({3})".format(prob_num,\
            #    num1, operator, num2, ))

            answer = 0
            if operator == '+':
                answer = num1 + num2
            else:
                answer = num1 - num2

            fkey.write("{0}.\t{1}\n".format(prob_num, answer))
                
            

    ## Close the Math key file
    fkey.close()


## Create user-defined number of math problems
num_problems = 100
fname_problems = createMathProblems(num_problems)

## Create answer key based on math problems created
fname_key = createAnswerKey(fname_problems, num_problems)
