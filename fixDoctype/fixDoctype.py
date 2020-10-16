import os
import sys
import pyinputplus as pyip
from lxml import etree
import xml.etree.ElementTree as et

##THIS PYTHON SCRIPT LETS YOU REPLACE THE
##DOCTYPE DECLARATIONS IN A SET OF XML FILES
##IT IS INTENDED FOR DITA FILES BUT SHOULD
##WORK FOR ANY XML FILES 

# Step 1: CHOOSE DIRECTORY CONTAINING THE FILES TO FIX
# C:\Users\jdwin\Documents\jdwinfodesign\doctype-python\src
def chooseDir(rootDir):
    print('You want to search: ' + rootDir + '?')
    print('Type \'y\' and ENTER to confirm, any other key to abort.')
    confirm = input()
    if confirm == 'y':
        print('ok')
        walk(rootDir)
    else:
            print('goodbye')

# Step 2: WALK THE CHOSEN DIRECTORY AND ALL SUBDIRECTORIES

def walk(rootDir, outdir):
    for subdir, dirs, files in os.walk(rootDir):
        for filename in files:
            filepath = subdir + os.sep + filename

            #if filepath.endswith(".jpg") or filepath.endswith(".png"):
            print ('filepath: ' + filepath)
            print ('filename: ' + filename)
            fixDoctype(rootDir, outdir, filename, filepath)

# Step 3: COPY EACH FILE IN THE DIRECTORY, REPLACING DOCTYPE

def fixDoctype(rootDir, outdir, filename, filepath):
##    print('rootDir: ' + rootDir)
##    print(' outdir: ' + outdir)

    parser = etree.XMLParser(strip_cdata=False)
    tree = etree.parse(filepath, parser)
##
    root = tree.getroot()
##
### TODO replace doctype with variable
    tree.write(outdir + '\\' + filename, xml_declaration=True, encoding='UTF-8', doctype='''<!DOCTYPE concept PUBLIC "urn:pubid:jdwinfodesign.com:doctypes:dita:dtd:concept" "concept.dtd">''')
# TODO replace doctype with variable
    print(' rootDir: ' + rootDir)
    print('  outdir: ' + outdir)
    print('filename: ' + filename)

#---------------------------------------------------------------------

print(r'Enter the absolute path to search. For example:')
print(r'C:\Users\jdwin\Documents\jdwinfodesign\doctype-python\walkTest')

rootDir = input()
##chooseDir(rootDir)

print('Enter the file path to the output directory')

outdir = input()
walk(rootDir, outdir)
