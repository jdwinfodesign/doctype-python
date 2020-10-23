import os
import sys
import pyinputplus as pyip
from lxml import etree
import shutil

## CHECK FOR FILE EXTENSION

# Step 2: COPY THE DIRECTORY TREE FROM INPUT DIRECTORY TO OUTPUT DIRECTORY

def copyDirs(inDir, outDir):
    shutil.copytree(inDir, outDir, dirs_exist_ok=True)
    walkTree(inDir, outDir)

def walkTree(inDir, outDir):
    xmlExt = ('dita', 'xml')
    for subdir, dirs, files in os.walk(outDir):
        for filename in files:
            filepath = subdir + os.sep + filename

            print(filepath)
            print(type(filepath))
            if filepath.endswith(xmlExt):
                print('A dita file')

#---------------------------------------------------------------------

# Step 0: Prompt user to choose directory containing
#         files to be modified (inDir) and
#         location for output (outDir)

inDir = r'C:\Users\jdwin\Documents\jdwinfodesign\doctype-python\copyDirs\src'
outDir = r'C:\Users\jdwin\Documents\jdwinfodesign\doctype-python\copyDirs\out'

copyDirs(inDir, outDir)

