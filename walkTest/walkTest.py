import os
from lxml import etree
import xml.etree.ElementTree as ET

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
    for subdir, dirs, files in os.walk(r'C:\Users\jdwin\Documents\jdwinfodesign\doctype-python\walkTest'):
        for filename in files:
            filepath = subdir + os.sep + filename

            #if filepath.endswith(".jpg") or filepath.endswith(".png"):
            print (filepath)
            #print (filename)
            
# doctypeFix(r'../src/c_about_defining_payload.dita')
# check()
# listdir()
# scandir()
walk()
