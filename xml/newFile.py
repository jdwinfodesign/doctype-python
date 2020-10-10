import os
import re
from lxml import etree

# root = etree.Element("concept")


#concept = etree.parse(r'.\src\test-30-c.dita')



##os.chdir('out')
##
##et = etree.ElementTree(root)
##et.write('foo.dita',xml_declaration = True, encoding='UTF-8', doctype='<!DOCTYPE concept PUBLIC "urn:pubid:jdwinfodesign.com:doctypes:dita:dtd:concept" "concept.dtd">')



# from stackoverflow
#Master XML
parser = etree.XMLParser(strip_cdata=False)
tree = etree.parse(r'.\src\test-30-c.dita', parser)
# Find the //input node - which has a lot of subelems
inputMaster= tree.xpath('//concept')[0]
print(etree.tostring(inputMaster,pretty_print=True,encoding='unicode'))
