# Seems to work

import os
import re

# Open file
#fin = open(r'C:\Users\jdwin\Documents\jdwinfodesign\doctype-python\str\src\test-10.dita','r')
#content = fin.read()
string = '''<!DOCTYPE concept PUBLIC "-//OASIS//DTD DITA Concept//EN"
"http://docs.oasis-open.org/dita/v1.1/OS/dtd/concept.dtd">'''

def check():
        with open(r'src\test-202.dita','r') as f:
                if string in f.read():
                        print("true")
                else:
                        print('false')

##def check():
##    datafile = open(r'src\test-10.dita')
##    datafile.read()
##    found = False
##    for line in datafile:
##        if blahblah in line:
##            found = True
##            break
##
check()


