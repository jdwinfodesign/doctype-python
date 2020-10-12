import os
import re
from lxml import etree

# from stackoverflow
#Master XML
parser = etree.XMLParser(strip_cdata=False)
tree = etree.parse(r'.\src\test-30-c.dita', parser)
# Find the //input node - which has a lot of subelems
root = tree.xpath('//concept')[0]
print(etree.tostring(root, pretty_print=True, encoding='unicode'))
print('===============================')
from xml.etree.ElementTree import parse, tostring
doc = parse(r'.\src\test-30-c.dita', parser)
title = tree.xpath('//title')[0]
title.text = 'New Title'
#print(etree.tostring(doc.getroot()))
print(etree.tostring(root, pretty_print=True, encoding='unicode'))


