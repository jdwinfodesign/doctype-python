# Seems to work

import os
import re
# TODO Define regex
# '^<!DOCTYPE concept.*>$' --> This one finds all variations 

# TODO Open file
# c_about_defining_payload.dita

file = open('C:\\Users\\jdwin\\Documents\\jdwinfodesign\\doctype-python\\src-use\\c_about_defining_payload.dita','r')
file_contents = file.read()
print(file_contents)
file.close()
# TODO Find string matching regex

# TODO Replace regex with new string

# TODO Save file with new string

