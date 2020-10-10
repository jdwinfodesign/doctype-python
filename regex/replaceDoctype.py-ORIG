# Seems to work

import os
import re

# Open file

file = open(r'C:\Users\jdwin\Documents\jdwinfodesign\doctype-python\regex\src-use\test-01.dita','r')
file_content = file.read()
# next line can verify file content for sanity check
# print(file_content) 

new = file_content
file.close()

# TODO Find the document type declaration
regexDoctype = re.compile('<!DOCTYPE concept.*\[[\s|\S]*\]>')
origDoctype = str(regexDoctype.findall(new))
print(origDoctype)

# TODO Strip extraneous chars from origDoctype string
# print(orig_text.strip('-$'))

cleanOrigDoctype = origDoctype.strip('\[\'\]')
print(cleanOrigDoctype)

#-------------------------------------

# TODO Define new doctype
# <!DOCTYPE concept PUBLIC "urn:pubid:jdwinfodesign.com:doctypes:dita:dtd:concept" "concept.dtd">
newDoctype = ('<!DOCTYPE concept PUBLIC "urn:pubid:jdwinfodesign.com:doctypes:dita:dtd:concept" "concept.dtd">')

#TODO Replace old doctype with new
replace=new.replace(origDoctype, newDoctype)
print(replace)

#-------------------------------------

# r'<!DOCTYPE concept PUBLIC "-//OASIS//DTD DITA Composite//EN" "ditabase.dtd" [\n\n<!-- Begin Document Specific Declarations -->\n\n\n<!-- End Document Specific Declarations -->\n\n]>'
# r'<!DOCTYPE concept PUBLIC "urn:pubid:jdwinfodesign.com:doctypes:dita:dtd:concept" "concept.dtd">'

#-------------------------------------

# TODO Open a new file

file = open(r'C:\Users\jdwin\Documents\jdwinfodesign\doctype-python\regex\out\test-02.dita','w')

# next line can verify file content for sanity check
# print(file_content) 

#-------------------------------------

# TODO Save file with new string


# \[[\s|\S]*\]
# <!DOCTYPE concept.*\[[\s|\S]*\]>
# <!DOCTYPE concept.*(\[[\s|\S]\])?>
