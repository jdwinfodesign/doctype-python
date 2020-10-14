import os
from lxml import etree
import xml.etree.ElementTree as ET

# --------------------------------------------------------------------------------
# COPY FILE WITH NEW DOCTYPE
# --------------------------------------------------------------------------------
# filename is passed from call to function below
def doctypeFix(filename):

    parser = etree.XMLParser(strip_cdata=False)
    tree = etree.parse(filename, parser)

    root = tree.getroot()

# TODO replace doctype with variable
    tree.write('out/c_about_defining_payload.dita', xml_declaration=True,
               encoding='UTF-8',
               doctype='''<!DOCTYPE concept PUBLIC "urn:pubid:jdwinfodesign.com:doctypes:dita:dtd:concept" "concept.dtd">''')

##<!DOCTYPE map PUBLIC "urn:pubid:jdwinfodesign.com:doctypes:dita:dtd:map" "map.dtd">
##<!DOCTYPE dita PUBLIC "urn:pubid:jdwinfodesign.com:doctypes:dita:dtd:ditabase" "ditabase.dtd">
##<!DOCTYPE topic PUBLIC "urn:pubid:jdwinfodesign.com:doctypes:dita:dtd:topic" "topic.dtd">
##<!DOCTYPE concept PUBLIC "urn:pubid:jdwinfodesign.com:doctypes:dita:dtd:concept" "concept.dtd">
##<!DOCTYPE task PUBLIC "urn:pubid:jdwinfodesign.com:doctypes:dita:dtd:generalTask" "generalTask.dtd">
##<!DOCTYPE task PUBLIC "urn:pubid:jdwinfodesign.com:doctypes:dita:dtd:task" "task.dtd">
##<!DOCTYPE reference PUBLIC "urn:pubid:jdwinfodesign.com:doctypes:dita:dtd:reference" "reference.dtd">

# --------------------------------------------------------------------------------
# CHECK ORIGINAL DOCTYPE
# --------------------------------------------------------------------------------
##<!DOCTYPE concept
##<!DOCTYPE task 
##<!DOCTYPE reference

string = r'<!DOCTYPE concept'

def check():
        with open(r'../src/c_about_defining_payload.dita','r') as f:
                if string in f.read():
                        doctypeFix(r'../src/c_about_defining_payload.dita')
                        print(string)
                else:
                        print('false')
                        
# --------------------------------------------------------------------------------
# TODO this is filename param; to be replaced by getting filenames from directory 
# doctypeFix(r'../src/c_about_defining_payload.dita')
# check()

# --------------------------------------------------------------------------------
# TODO Iterate over all files in directory
# C:\Users\jdwin\Documents\jdwinfodesign\doctype-python\src
def listdir():
    directory = r'C:\Users\jdwin'
    for filename in os.listdir(directory):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            print(os.path.join(directory, filename))
        else:
            continue
        
def scandir():
    directory = r'C:\Users\jdwin'
    for entry in os.scandir(directory):
        if (entry.path.endswith(".jpg")
                or entry.path.endswith(".png")) and entry.is_file():
            print(entry.path)

def walk():
    for subdir, dirs, files in os.walk(r'C:\Users\jdwin\Documents\jdwinfodesign\doctype-python\src'):
        for filename in files:
            filepath = subdir + os.sep + filename

            #if filepath.endswith(".jpg") or filepath.endswith(".png"):
            print (filepath)
            #print (filename)
##listdir()
##scandir()
walk()
