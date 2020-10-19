import os
import sys
import pyinputplus as pyip
from lxml import etree

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
    genTaskString = '''generalTask'''

    print(r'      root_name: ' + docinfo.root_name)
##
    root = tree.getroot()

    if docinfo.root_name == 'concept':
            newDoctype = '''<!DOCTYPE concept PUBLIC "urn:pubid:jdwinfodesign.com:doctypes:dita:dtd:concept" "concept.dtd">'''
    elif docinfo.root_name == 'task':
                if genTaskString in docinfo.doctype:
                        newDoctype = '''<!DOCTYPE task PUBLIC "urn:pubid:jdwinfodesign.com:doctypes:dita:dtd:generalTask" "generalTask.dtd">'''
                else:
                        newDoctype = '''<!DOCTYPE task PUBLIC "urn:pubid:jdwinfodesign.com:doctypes:dita:dtd:task" "task.dtd">'''
    elif docinfo.root_name == 'reference':
            newDoctype = '''<!DOCTYPE reference PUBLIC "urn:pubid:jdwinfodesign.com:doctypes:dita:dtd:reference" "reference.dtd">'''
    elif docinfo.root_name == 'map':
            newDoctype = '''<!DOCTYPE map PUBLIC "urn:pubid:jdwinfodesign.com:doctypes:dita:dtd:map" "map.dtd">'''
    elif docinfo.root_name == 'dita':
            newDoctype = '''<!DOCTYPE dita PUBLIC "urn:pubid:jdwinfodesign.com:doctypes:dita:dtd:ditabase" "ditabase.dtd">'''
    elif docinfo.root_name == 'topic':
            newDoctype = '''<!DOCTYPE topic PUBLIC "urn:pubid:jdwinfodesign.com:doctypes:dita:dtd:topic" "topic.dtd">'''
    else:
                print(r'root_name not in list')
            
            


    
    tree.write(outDir + '\\' + filename, xml_declaration=True, encoding='UTF-8', doctype=newDoctype)

# TODO replace doctype with variable
    
##    print('   inDir: ' + inDir)
##    print('  outDir: ' + outDir)
##    print('filename: ' + filename)
    print()

##============================================================================================
## <!DOCTYPE task PUBLIC "-//OASIS//DTD DITA General Task//EN" "generalTask.dtd">
##<!DOCTYPE task PUBLIC "urn:pubid:jdwinfodesign.com:doctypes:dita:dtd:generalTask" "generalTask.dtd">


##<!DOCTYPE map PUBLIC "urn:pubid:jdwinfodesign.com:doctypes:dita:dtd:map" "map.dtd">
##<!DOCTYPE dita PUBLIC "urn:pubid:jdwinfodesign.com:doctypes:dita:dtd:ditabase" "ditabase.dtd">
##<!DOCTYPE topic PUBLIC "urn:pubid:jdwinfodesign.com:doctypes:dita:dtd:topic" "topic.dtd">
##<!DOCTYPE concept PUBLIC "urn:pubid:jdwinfodesign.com:doctypes:dita:dtd:concept" "concept.dtd">

##<!DOCTYPE task PUBLIC "urn:pubid:jdwinfodesign.com:doctypes:dita:dtd:task" "task.dtd">
##<!DOCTYPE reference PUBLIC "urn:pubid:jdwinfodesign.com:doctypes:dita:dtd:reference" "reference.dtd">
##============================================================================================

inDir = r'C:\Users\jdwin\Documents\jdwinfodesign\doctype-python\ifForDoctype\src'
outDir = r'C:\Users\jdwin\Documents\jdwinfodesign\doctype-python\ifForDoctype\out'

##check()
##walk(inDir, outDir)
walkDoctype(inDir, outDir)
##parseFile
