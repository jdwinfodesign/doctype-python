# Seems to work

import os
import re
from lxml import etree


# to open the file below
from io import BytesIO
# BELOW is from lxml tutorial
##file = BytesIO(b'<concept><title>Company Name</title></concept>')
##tree = etree.parse(file)
##etree.tostring(tree)

# below is answer from stackoverload thread
root = etree.parse(r'src\4etree.dita')
# Print the loaded XML
print(etree.tostring(root,pretty_print=True,encoding='unicode'))





# >>> print(etree.tostring(root, pretty_print=True))
#   b'<root>\n  <child1/>\n  <child2/>\n  <child3/>\n</root>\n'
# The 'b' at the beginning shows it is a byte string, so it does
# not indent as intended
# To make it look like the tutorial, add encoding as follows:
# print(etree.tostring(root,pretty_print=True,encoding='unicode'))
##root = etree.Element("root")
##
##child1 = etree.SubElement(root,"child1")
##child2 = etree.SubElement(root, "child2")
##child3 = etree.SubElement(root, "child3")
##print(etree.tostring(root,pretty_print=True,encoding='unicode'))

# Open file

##file = open('src\\test-202.dita','rb')
##content = file.read()
##
##new = content
#file.close()

# TODO Find the document type declaration
##regexDoctype = re.compile(r'<!DOCTYPE concept.*\s*\S*>')
##origDoctype = regexDoctype.findall(new)
##print(origDoctype)

#regexDoctype = re.compile(r'<!DOCTYPE concept.*\[[\s|\S]*\]>')
# first capturing group
# (\[?[\s|\S]*\]?)?
# file.close()

# test-20.dita
# ['<!DOCTYPE concept PUBLIC "-//OASIS//DTD DITA Concept//EN" "http://docs.oasis-open.org/dita/v1.1/OS/dtd/concept.dtd">']
# test-201.dita
# ['<!DOCTYPE concept PUBLIC "-//OASIS//DTD DITA Concept//EN" ']
# test-202.dita
# ['<!DOCTYPE concept PUBLIC "-//OASIS//DTD DITA Concept//EN"']
