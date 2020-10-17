import os
import sys
import pyinputplus as pyip
from lxml import etree
import xml.etree.ElementTree as et

# Open file
#fin = open(r'C:\Users\jdwin\Documents\jdwinfodesign\doctype-python\str\src\test-10.dita','r')
#content = fin.read()
string = '''<!DOCTYPE concept'''

def check():
        with open(r'src\c_architecture_overview.dita','r') as f:
                if string in f.read():
                        print("true")
                else:
                        print('false')

## - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def walk(inDir, outDir):
    for subdir, dirs, files in os.walk(inDir):
        for filename in files:
            filepath = subdir + os.sep + filename

            #if filepath.endswith(".jpg") or filepath.endswith(".png"):
##            print()
##            print ('filepath: ' + filepath)
##            print ('filename: ' + filename)
##            print()
            parseFile(inDir, outDir, filename, filepath)
            
## - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def parseFile(inDir, outDir, filename, filepath):
##    print('inDir: ' + inDir)
##    print(' outDir: ' + outDir)

    parser = etree.XMLParser(strip_cdata=False)
    tree = etree.parse(filepath, parser)
    docinfo = tree.docinfo
    print(r'======================================')
    print()
    print(r'            URL: ' + docinfo.URL)
    print(r'     system_url: ' + docinfo.system_url)
    print(r'        doctype: ' + docinfo.doctype)
    print(r'      public_id: ' + docinfo.public_id)
    print(r'      root_name: ' + docinfo.root_name)
##
    root = tree.getroot()

##
### TODO replace doctype with variable
    tree.write(outDir + '\\' + filename, xml_declaration=True, encoding='UTF-8', doctype='''<!DOCTYPE concept PUBLIC "urn:pubid:jdwinfodesign.com:doctypes:dita:dtd:concept" "concept.dtd">''')

# TODO replace doctype with variable
    
##    print('   inDir: ' + inDir)
##    print('  outDir: ' + outDir)
##    print('filename: ' + filename)
    print()

##============================================================================================
##============================================================================================

def walkDoctype(inDir, outDir):
    for subdir, dirs, files in os.walk(inDir):
        for filename in files:
            filepath = subdir + os.sep + filename

            #if filepath.endswith(".jpg") or filepath.endswith(".png"):
##            print()
##            print ('filepath: ' + filepath)
##            print ('filename: ' + filename)
##            print()
            parseDoctype(inDir, outDir, filename, filepath)

def parseDoctype(inDir, outDir, filename, filepath):
##    print('inDir: ' + inDir)
##    print(' outDir: ' + outDir)

    parser = etree.XMLParser(strip_cdata=False)
    tree = etree.parse(filepath, parser)
    docinfo = tree.docinfo
    print(r'======================================')
    print()
    print(r'            URL: ' + docinfo.URL)
    print(r'     system_url: ' + docinfo.system_url)
    print(r'        doctype: ' + docinfo.doctype)
    print(r'      public_id: ' + docinfo.public_id)
    print(r'      root_name: ' + docinfo.root_name)
##
    root = tree.getroot()

##
### TODO replace doctype with variable
    tree.write(outDir + '\\' + filename, xml_declaration=True, encoding='UTF-8', doctype='''<!DOCTYPE concept PUBLIC "urn:pubid:jdwinfodesign.com:doctypes:dita:dtd:concept" "concept.dtd">''')

# TODO replace doctype with variable
    
##    print('   inDir: ' + inDir)
##    print('  outDir: ' + outDir)
##    print('filename: ' + filename)
    print()

##============================================================================================
##============================================================================================

inDir = r'C:\Users\jdwin\Documents\jdwinfodesign\doctype-python\chooseDoctype\src'
outDir = r'C:\Users\jdwin\Documents\jdwinfodesign\doctype-python\chooseDoctype\out'

##check()
##walk(inDir, outDir)
walkDoctype(inDir, outDir)
##parseFile
