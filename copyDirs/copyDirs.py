import os
import sys
import pyinputplus as pyip
from lxml import etree
import shutil

def copyDirs(inDir, outDir):
    shutil.copytree(inDir, outDir, dirs_exist_ok=True)

#--------------------------------------------------------------------------------

def walkDoctype(inDir, outDir):
    for subdir, dirs, files in os.walk(outDir):
        for filename in files:
            filepath = subdir + os.sep + filename

            fixDoctype(outDir, filename, filepath)

def fixDoctype(outDir, filename, filepath):

    parser = etree.XMLParser(strip_cdata=False)
    tree = etree.parse(filepath, parser)
    docinfo = tree.docinfo
    genTaskString = '''generalTask'''

    if docinfo.root_name == 'concept':
            newDoctype = '''<!DOCTYPE concept PUBLIC "urn:pubid:jdwinfodesign.com:doctypes:dita:dtd:concept" "concept.dtd">'''
            print(r'Writing new doctype to ' + filepath)
    elif docinfo.root_name == 'task':
        if genTaskString in docinfo.doctype:
            newDoctype = '''<!DOCTYPE task PUBLIC "urn:pubid:jdwinfodesign.com:doctypes:dita:dtd:generalTask" "generalTask.dtd">'''
        else:
            newDoctype = '''<!DOCTYPE task PUBLIC "urn:pubid:jdwinfodesign.com:doctypes:dita:dtd:task" "task.dtd">'''
            print(r'Writing new doctype to ' + filepath)
    elif docinfo.root_name == 'reference':
            newDoctype = '''<!DOCTYPE reference PUBLIC "urn:pubid:jdwinfodesign.com:doctypes:dita:dtd:reference" "reference.dtd">'''
            print(r'Writing new doctype to ' + filepath)
    elif docinfo.root_name == 'map':
            newDoctype = '''<!DOCTYPE map PUBLIC "urn:pubid:jdwinfodesign.com:doctypes:dita:dtd:map" "map.dtd">'''
            print(r'Writing new doctype to ' + filepath)
    elif docinfo.root_name == 'dita':
            newDoctype = '''<!DOCTYPE dita PUBLIC "urn:pubid:jdwinfodesign.com:doctypes:dita:dtd:ditabase" "ditabase.dtd">'''
            print(r'Writing new doctype to ' + filepath)
    elif docinfo.root_name == 'topic':
            newDoctype = '''<!DOCTYPE topic PUBLIC "urn:pubid:jdwinfodesign.com:doctypes:dita:dtd:topic" "topic.dtd">'''
            print(r'Writing new doctype to ' + filepath)
    else:
                print(r'root_name not in list')
                
    tree.write(filepath, xml_declaration=True, encoding='UTF-8', doctype=newDoctype)

#--------------------------------------------------------------------------------

print(r'Enter the absolute path to the directory containing files to modify. For example:')
print(r'C:\Users\jdwin\Documents\XMLfiles\src')

inDir = r'C:\Users\jdwin\Documents\jdwinfodesign\doctype-python\copyDirs\src'
outDir = r'C:\Users\jdwin\Documents\jdwinfodesign\doctype-python\copyDirs\out'
copyDirs(inDir, outDir)
walkDoctype(inDir, outDir)
