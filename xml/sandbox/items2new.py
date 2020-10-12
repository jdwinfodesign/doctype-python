import os
from lxml import etree
import xml.etree.ElementTree as ET

parser = etree.XMLParser(strip_cdata=False)
tree = etree.parse(r'concept-00.dita', parser)

#tree = ET.parse('concept-00.dita')

root = tree.getroot()

### changing a field text
##for elem in root.iter('item'):
##    elem.text = 'new text'
##
### modifying an attribute
##for elem in root.iter('item'):
##    elem.set('name', 'newitem')
##
### adding an attribute
##for elem in root.iter('item'):
##    elem.set('name2', 'newitem2')

tree.write('newConcept-00.dita', xml_declaration=True, encoding='UTF-8', doctype='<!DOCTYPE concept PUBLIC "urn:pubid:jdwinfodesign.com:doctypes:dita:dtd:concept" "concept.dtd">')
