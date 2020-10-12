import os
import re
from lxml import etree

root = etree.Element('concept')
print('Root tag: ' + root.tag)
print('=================')

root.append(etree.Element('title'))
# following is shortcut for root.append
child2 = etree.SubElement(root, "shortdesc")
child3 = etree.SubElement(root, "conbody")

print(etree.tostring(root,pretty_print=True, encoding='unicode'))
