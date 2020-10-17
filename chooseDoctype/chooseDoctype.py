import os
import sys
import pyinputplus as pyip
from lxml import etree
import xml.etree.ElementTree as et

##THIS PYTHON SCRIPT LETS YOU REPLACE THE
##DOCTYPE DECLARATIONS IN A SET OF XML FILES
##IT IS INTENDED FOR DITA FILES BUT SHOULD
##WORK FOR ANY XML FILES 

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
    tree.write(outDir + '\\' + filename, xml_declaration=True, encoding='UTF-8', doctype='''<!DOCTYPE concept PUBLIC "urn:pubid:jdwinfodesign.com:doctypes:dita:dtd:concept" "concept.dtd">''')
# TODO replace doctype with variable
    print(' inDir: ' + inDir)
    print('  outDir: ' + outDir)
    print('filename: ' + filename)

#--------------------------------------------------------------------------------
inDir =
outDir = 

walk(inDir)


##<!DOCTYPE map PUBLIC "urn:pubid:jdwinfodesign.com:doctypes:dita:dtd:map" "map.dtd">
##<!DOCTYPE dita PUBLIC "urn:pubid:jdwinfodesign.com:doctypes:dita:dtd:ditabase" "ditabase.dtd">
##<!DOCTYPE topic PUBLIC "urn:pubid:jdwinfodesign.com:doctypes:dita:dtd:topic" "topic.dtd">
##<!DOCTYPE concept PUBLIC "urn:pubid:jdwinfodesign.com:doctypes:dita:dtd:concept" "concept.dtd">
##<!DOCTYPE task PUBLIC "urn:pubid:jdwinfodesign.com:doctypes:dita:dtd:generalTask" "generalTask.dtd">
##<!DOCTYPE task PUBLIC "urn:pubid:jdwinfodesign.com:doctypes:dita:dtd:task" "task.dtd">
##<!DOCTYPE reference PUBLIC "urn:pubid:jdwinfodesign.com:doctypes:dita:dtd:reference" "reference.dtd">

