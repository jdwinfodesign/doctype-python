# Seems to work

import os
import re
# TODO Define regex
# '^<!DOCTYPE concept.*>$' --> This one finds all variations 

# TODO Open file
# c_about_defining_payload.dita

file = open('C:\\Users\\jdwin\\Documents\\jdwinfodesign\\doctype-python\\src-use\\c_about_defining_payload.dita','r')
file_content = file.read()

# TODO Find string the document type declaration
findDoctype = re.compile('<!DOCTYPE concept.*(>?)', re.DOTALL)
print(findDoctype.search(file_content))
print(file_content)
file.close()

#-------------------------------------
file = open('C:\\Users\\jdwin\\Documents\\jdwinfodesign\\doctype-python\\src-use\\c_about_defining_payload.dita','r')
file_content = file.read()
findShitString = re.compile(r'\[.*[\r\n]*.*')
shitString = findShitString.findall(file_content)
print(shitString)
subShitString = re.sub(findShitString,'foo',file_content)
print(shitString(re.sub('Begin','Foo')))
print(findShitString.search(file_content))

replaceShitString = findShitString.sub

#-------------------------------------

# TODO Replace regex with new string

# TODO Save file with new string

findDoctype = re.compile(r'<!DOCTYPE.*[\r\n]*.*[\r\n]*.*[\r\n]*.*]>', re.DOTALL)
f = findDoctype.findall(r'<!DOCTYPE concept PUBLIC "-//OASIS//DTD DITA Composite//EN" "ditabase.dtd" \]\n<!-- Begin Document Specific Declarations -->\n\n<!-- End Document Specific Declarations -->\n\]>')
f


<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE concept PUBLIC "-//OASIS//DTD DITA Composite//EN" "ditabase.dtd"
#<!DOCTYPE.*[\r\n]*.*[\r\n]*.*[\r\n]*.*]>

AttributeError: 'list' object has no attribute 'sub'
>>> print(shitString(re.sub('Begin','Foo')))
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    print(shitString(re.sub('Begin','Foo')))
TypeError: sub() missing 1 required positional argument: 'string'
>>> subShitString = re.sub(r'[\n\n<!-- Begin Document Specific Declarations -->[\1]','foo')
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    subShitString = re.sub(r'[\n\n<!-- Begin Document Specific Declarations -->[\1]','foo')
TypeError: sub() missing 1 required positional argument: 'string'
>>> subShitString = re.sub(findShitString,'foo',file_content)
>>> subShitString

>>> os.chdir(r'C:\Users\jdwin\Documents\jdwinfodesign\doctype-python\out')
>>> os.getcwd
<built-in function getcwd>
>>> os.getcwd()
'C:\\Users\\jdwin\\Documents\\jdwinfodesign\\doctype-python\\out'
>>> newFile = open('new.txt','w')
>>> newFile.write(subShitString)
12583
>>> 
