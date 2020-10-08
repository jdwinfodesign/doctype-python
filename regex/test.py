import os
import re

#input file
##fin = open(r'C:\Users\jdwin\Documents\jdwinfodesign\doctype-python\regex\src-use\foo.dita','r')
##fin_content = fin.read()
##
##regexDoctype = re.compile(r'<!DOCTYPE concept.*\[?[\s|\S]*\]?>')
##origDoctype = str(regexDoctype.findall(fin_content))

##regexDoctype = re.compile(r'<!DOCTYPE concept.*\[?[\s|\S]*\]?>')
##origDoctype = str(regexDoctype.findall(fin_content))

fin = open(r'C:\Users\jdwin\Documents\jdwinfodesign\doctype-python\regex\src-use\foo.dita','r')
fin_content = fin.read()
regexDoctype = re.compile(r'<!DOCTYPE concept.*\[?[\s|\S]*\]?>')
origDoctype = str(regexDoctype.findall(fin_content))

if 'origDoctype' in fin.read():
    print(origDoctype)
else:
    print('Not found')



