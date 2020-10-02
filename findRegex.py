# Seems to work

import os
import re
# TODO Define regex
# '^<!DOCTYPE concept.*>$' --> This one finds all variations 

# TODO Open file
# c_about_defining_payload.dita

file = open('C:\\Users\\jdwin\\Documents\\jdwinfodesign\\doctype-python\\src-use\\c_about_defining_payload.dita','r')
file_contents = file.read()

# TODO Find string matching regex
findDoctype = re.compile(r'<!DOCTYPE concept.*>$', re.DOTALL)
print(findDoctype.search(file_contents))
print(file_contents)
file.close()

# TODO Replace regex with new string

# TODO Save file with new string

foo = re.compile(r'<!DOCTYPE>?')
f = foo.findall(r'   <!DOCTYPE          >')
f


<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE concept PUBLIC "-//OASIS//DTD DITA Composite//EN" "ditabase.dtd"
