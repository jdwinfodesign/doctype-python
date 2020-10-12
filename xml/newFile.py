import os
import re
from lxml import etree

#==============================
# parse file
parser = etree.XMLParser(strip_cdata=False)
##
## tree is the entire tree of the file we are parsing
## root is the root element of the file
tree = etree.parse(r'.\src\test-30-c.dita', parser)
root = tree.xpath('//concept')[0]
print(etree.tostring(root, pretty_print=True, encoding='unicode'))

#==============================
# create new document

rootElement = etree.Element('concept')

os.chdir('out')
# output the new document

elem = root.xpath('//title')[0]
elem.text = 'New Title'

etreeElementTree = etree.ElementTree(rootElement)
etreeElementTree.write('foo.dita',xml_declaration=True, encoding='UTF-8',
    doctype='<!DOCTYPE concept PUBLIC "urn:pubid:jdwinfodesign.com:doctypes:dita:dtd:concept" "concept.dtd">')

