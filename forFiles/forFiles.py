import os
from lxml import etree
import xml.etree.ElementTree as ET

def doctypeFix(filename):

    parser = etree.XMLParser(strip_cdata=False)
    tree = etree.parse(filename, parser)

    root = tree.getroot()

    tree.write('out/c_about_defining_payload.dita', xml_declaration=True,
               encoding='UTF-8',
               doctype='''<!DOCTYPE concept PUBLIC "urn:pubid:jdwinfodesign.com:doctypes:dita:dtd:concept" "concept.dtd">''')

doctypeFix(r'../src/c_about_defining_payload.dita')
