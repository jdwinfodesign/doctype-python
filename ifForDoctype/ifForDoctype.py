import os
import sys
import pyinputplus as pyip
from lxml import etree
import xml.etree.ElementTree as et

##THIS PYTHON SCRIPT LETS YOU REPLACE THE
##DOCTYPE DECLARATIONS IN A SET OF XML FILES
##IT IS INTENDED PRIMARILY FOR DITA FILES 

# Step 1: CONFIRM DIRECTORIES CHOSEN
def verifyDirs(inDir):
    print('You want to modify the files in: ' + inDir + '?')
    print('Type \'y\' and ENTER to confirm, any other key to abort.')
    confirmInDir = input()
    if confirmInDir == 'y':
        print(r'Enter the absolute path to direct the output. For example:')
        print(r'C:\Users\jdwin\Documents\XMLfiles\out')
        outDir = input()
        print('You want to direct the output to: ' + outDir + '?')
        print('Type \'y\' and ENTER to confirm, any other key to abort.')
        confirmOutDir = input()
        if confirmOutDir == 'y':
            print('OK')
            walk(inDir, outDir)
        else:
            print('Goodbye')
        
    else:
            print('Goodbye')

# Step 2: WALK THE CHOSEN DIRECTORY AND ALL SUBDIRECTORIES

def walk(inDir, outDir):
    for subdir, dirs, files in os.walk(inDir):
        for filename in files:
            filepath = subdir + os.sep + filename

            #if filepath.endswith(".jpg") or filepath.endswith(".png"):
            print ('filepath: ' + filepath)
            print ('filename: ' + filename)
            fixDoctype(inDir, outDir, filename, filepath)

# Step 3: COPY EACH FILE IN THE DIRECTORY, REPLACING DOCTYPE

def fixDoctype(inDir, outDir, filename, filepath):
##    print('inDir: ' + inDir)
##    print(' outDir: ' + outDir)

    parser = etree.XMLParser(strip_cdata=False)
    tree = etree.parse(filepath, parser)
##
    root = tree.getroot()
##
### TODO replace doctype with variable
### TODO: MAKE DIR IF NONE EXISTS
    tree.write(outDir + '\\' + filename, xml_declaration=True, encoding='UTF-8', doctype='''<!DOCTYPE concept PUBLIC "urn:pubid:jdwinfodesign.com:doctypes:dita:dtd:concept" "concept.dtd">''')

    print(' inDir: ' + inDir)
    print('  outDir: ' + outDir)
    print('filename: ' + filename)

#--------------------------------------------------------------------------------
# Step 0: Prompt user to choose directory containing
#         files to be modified (inDir) and
#         location for output (outDir)

print(r'Enter the absolute path to the directory containing files to modify. For example:')
print(r'C:\Users\jdwin\Documents\XMLfiles\src')

inDir = input()

verifyDirs(inDir)
