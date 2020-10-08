# Seems to work

import os
import re

# Open file
# <!DOCTYPE concept PUBLIC "-//OASIS//DTD DITA Concept//EN" "concept.dtd">

#input file
fin = open(r'C:\Users\jdwin\Documents\jdwinfodesign\doctype-python\regex\src-use\test.dita','r')
fin_content = fin.read()

#output file
fout = open(r'C:\Users\jdwin\Documents\jdwinfodesign\doctype-python\regex\out\test.dita','w')

##regexDoctype = re.compile(r'<!DOCTYPE concept.*\[?[\s|\S]*\]?>')
##origDoctype = str(regexDoctype.findall(fin_content))
##
##cleanOrigDoctype = origDoctype.strip('\[\'\]')
##cleanOrigDoctype
#-------------------------------------------------------------------------
#newDoctype = (r'<!DOCTYPE concept PUBLIC "urn:pubid:jdwinfodesign.com:doctypes:dita:dtd:concept" "concept.dtd">')
#-------------------------------------------------------------------------
for line in fin:
	#read replace the string and write to output
	fout.write(line.replace(r'foo','bar'))
fin.close()
fout.close()
