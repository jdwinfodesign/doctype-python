import os
import re

#input file
fin = open(r'C:\Users\jdwin\Documents\jdwinfodesign\doctype-python\regex\out\foo.dita','r')
content = fin.read()

regex = re.compile(r'<!DOCTYPE concept.*\[?[\s|\S]*\]?>')

new = re.sub(regex,'foo',content)


#output file
#fout = open(r'C:\Users\jdwin\Documents\jdwinfodesign\doctype-python\regex\out\bar.dita','w')
#for line in fin:
#    fout.write(line.sub(r'<!DOCTYPE concept.*\[?[\s|\S]*\]?>','<!DOCTYPE concept PUBLIC "urn:pubid:jdwinfodesign.com:doctypes:dita:dtd:concept" "concept.dtd">',str,0,re.DOTALL))
#fin.close()
#fout.close()
