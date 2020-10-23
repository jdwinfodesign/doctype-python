import os
import sys
import pyinputplus as pyip
from lxml import etree
import shutil

##REPLACE THE DOCTYPE DECLARATIONS IN A SET OF XML FILES

# Step 1: VERIFY THE INPUT (CHOSEN WHEN THE PROGRAM STARTS)
#         THEN ENTER THE OUTPUT DIRECTORY AND START PROCESSING

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
            copyDirs(inDir, outDir)
        else:
            print('Goodbye')
        
    else:
            print('Goodbye')

# Step 2: COPY THE DIRECTORY TREE FROM INPUT DIRECTORY TO OUTPUT DIRECTORY

def copyDirs(inDir, outDir):
        
    shutil.copytree(inDir, outDir, dirs_exist_ok=True)
    walkDoctype(inDir, outDir)

# Step 3: WALK THE OUTPUT DIRECTORY TO GET THE FILEPATH INFO FOR VARIABLES
#         THEN CALL THE FIXDOCTYPE FUNCTION

def walkDoctype(inDir, outDir):

##/._*/ and delete veto files options in our smb.conf to prevent creation of such files. Instead we leave .DS_STORE
    macRes = ('._', '.DS_Store')
    xmlExt = ('ditamap', 'dita', 'xml')
    
    for subdir, dirs, files in os.walk(outDir):
        for filename in files:
            filepath = subdir + os.sep + filename
            if not filename.startswith(macRes):
                if filepath.endswith(xmlExt):
                    fixDoctype(outDir, filename, filepath)


# Step 4: COPY EACH FILE IN THE DIRECTORY, REPLACING DOCTYPE

def fixDoctype(outDir, filename, filepath):

    parser = etree.XMLParser(strip_cdata=False)
    tree = etree.parse(filepath, parser)
    docinfo = tree.docinfo
    genTaskString = '''generalTask'''
    classifyMapString = '''subjectScheme'''

    if docinfo.root_name == 'concept':
            newDoctype = '''<!DOCTYPE concept PUBLIC "urn:pubid:jdwinfodesign.com:doctypes:dita:dtd:concept" "concept.dtd">'''
            print(r'Writing new doctype to ' + filepath)
    elif docinfo.root_name == 'task':
        if genTaskString in docinfo.doctype:
            newDoctype = '''<!DOCTYPE task PUBLIC "urn:pubid:jdwinfodesign.com:doctypes:dita:dtd:generalTask" "generalTask.dtd">'''
            print(r'Writing new doctype to ' + filepath)
        else:
            newDoctype = '''<!DOCTYPE task PUBLIC "urn:pubid:jdwinfodesign.com:doctypes:dita:dtd:task" "task.dtd">'''
            print(r'Writing new doctype to ' + filepath)
    elif docinfo.root_name == 'reference':
            newDoctype = '''<!DOCTYPE reference PUBLIC "urn:pubid:jdwinfodesign.com:doctypes:dita:dtd:reference" "reference.dtd">'''
            print(r'Writing new doctype to ' + filepath)
    elif docinfo.root_name == 'map':
        if classifyMapString in docinfo.doctype:
            newDoctype = '''<!DOCTYPE map PUBLIC "urn:pubid:jdwinfodesign.com:doctypes:dita:dtd:classifyMap" "classifyMap.dtd">'''
            print(r'Writing new doctype to ' + filepath)
        else: 
            newDoctype = '''<!DOCTYPE map PUBLIC "urn:pubid:jdwinfodesign.com:doctypes:dita:dtd:map" "map.dtd">'''
            print(r'Writing new doctype to ' + filepath)
    elif docinfo.root_name == 'dita':
            newDoctype = '''<!DOCTYPE dita PUBLIC "urn:pubid:jdwinfodesign.com:doctypes:dita:dtd:ditabase" "ditabase.dtd">'''
            print(r'Writing new doctype to ' + filepath)
    elif docinfo.root_name == 'subjectScheme':
            newDoctype = '''<!DOCTYPE subjectScheme PUBLIC "urn:pubid:jdwinfodesign.com:doctypes:dita:dtd:subjectScheme" "subjectScheme.dtd">'''
            print(r'Writing new doctype to ' + filepath)
    elif docinfo.root_name == 'topic':
            newDoctype = '''<!DOCTYPE topic PUBLIC "urn:pubid:jdwinfodesign.com:doctypes:dita:dtd:topic" "topic.dtd">'''
            print(r'Writing new doctype to ' + filepath)
    elif docinfo.root_name == 'glossentry':
            newDoctype = '''<!DOCTYPE glossentry PUBLIC "urn:pubid:jdwinfodesign.com:doctypes:dita:dtd:glossentry" "glossary.dtd">'''
            print(r'Writing new doctype to ' + filepath)
    elif docinfo.root_name == 'troubleshooting':
            newDoctype = '''<!DOCTYPE troubleshooting PUBLIC "urn:pubid:jdwinfodesign.com:doctypes:dita:dtd:troubleshooting" "troubleshooting.dtd">'''
            print(r'Writing new doctype to ' + filepath)
    else:
                print(r'root_name not in list')
                
    tree.write(filepath, xml_declaration=True, encoding='UTF-8', doctype=newDoctype)

#---------------------------------------------------------------------

# Step 0: Prompt user to choose directory containing
#         files to be modified (inDir) and
#         location for output (outDir)

print(r'Enter the absolute path to the directory containing files to modify. For example:')
print(r'C:\Users\jdwin\Documents\XMLfiles\src')

inDir = input()

verifyDirs(inDir)

