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
root = etree.parse(r'src\test-30-c.dita')
# Print the loaded XML
# The lxml tutorial did not produce results as shown in its example
# print(etree.tostring(root,pretty_print=True))
# I found the following, which produces a tree, in stackoverflow
# Interestingly, the pretty print seems useless
# The encoding is what makes the tree print as a tree, instead
# of a string with '\n' in place of whitespace
print(etree.tostring(root,pretty_print=True,encoding='unicode'))
##>>> docinfo=root.docinfo
##>>> docinfo
##<lxml.etree.DocInfo object at 0x000002483FD34FA0>
##>>> docinfo.doctype
##'<!DOCTYPE concept PUBLIC "-//OASIS//DTD DITA Concept//EN" "concept.dtd">'
##>>>


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
