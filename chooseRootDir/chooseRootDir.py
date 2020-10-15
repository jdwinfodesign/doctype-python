import os
import sys
import pyinputplus as pyip
from lxml import etree
import xml.etree.ElementTree as ET

# C:\Users\jdwin\Documents\jdwinfodesign\doctype-python\src
def walk(rootDir):
    print('You want to search: ' + rootDir + '?')
    confirm = input()
    if confirm == 'y':
        print('ok')
    else:
            print('goodbye')
##    print('If this is incorrect, please quit, then restart and enter the directory.')

##    for subdir, dirs, files in os.walk(r'C:\Users\jdwin\Documents\jdwinfodesign\doctype-python\walkTest'):
##        for filename in files:
##            filepath = subdir + os.sep + filename
##
##            #if filepath.endswith(".jpg") or filepath.endswith(".png"):
##            print (filepath)
##            #print (filename)

##walk()

def foo(rootDir):
    print('Hello ' + rootDir)


##pyip.inputFilepath(prompt='Input file path\n',
##                   postValidateApplyFunc=foo(rootDir),
##                   mustExist=True)

print(r'Enter the absolute path to search. For example:')
print(r'C:\Users\jdwin\Documents\jdwinfodesign\doctype-python\walkTest')

rootDir = input()
walk(rootDir)
