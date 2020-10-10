# Seems to work

import os
import re

# Open file

file = open(r'src\test-202.dita','r')
content = file.read()

new = content
#file.close()

# TODO Find the document type declaration
regexDoctype = re.compile(r'<!DOCTYPE concept.*\s*\S*>')
origDoctype = str(regexDoctype.findall(new))
print(origDoctype)

#regexDoctype = re.compile(r'<!DOCTYPE concept.*\[[\s|\S]*\]>')
# first capturing group
# (\[?[\s|\S]*\]?)?
file.close()

# test-20.dita
# ['<!DOCTYPE concept PUBLIC "-//OASIS//DTD DITA Concept//EN" "http://docs.oasis-open.org/dita/v1.1/OS/dtd/concept.dtd">']
# test-201.dita
# ['<!DOCTYPE concept PUBLIC "-//OASIS//DTD DITA Concept//EN" ']
# test-202.dita
# ['<!DOCTYPE concept PUBLIC "-//OASIS//DTD DITA Concept//EN"']
