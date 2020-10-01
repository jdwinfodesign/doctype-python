# Seems to work
import re

#doctype = '<!DOCTYPE concept PUBLIC "-//OASIS//DTD DITA Concept//EN" "concept.dtd">'
doctype2 = '''<!DOCTYPE concept PUBLIC "-//OASIS//DTD DITA Composite//EN" "ditabase.dtd" /n[
<!-- Begin Document Specific Declarations -->


<!-- End Document Specific Declarations -->

]>'''
##beginsWithDoctype = re.compile(r'^<!DOCTYPE concept')
##print (beginsWithDoctype.search(doctype))
# <!DOCTYPE concept PUBLIC "-//OASIS//DTD DITA Concept//EN" "concept.dtd">

##<!DOCTYPE concept PUBLIC "-//OASIS//DTD DITA Composite//EN" "ditabase.dtd" [
##
##<!-- Begin Document Specific Declarations -->
##
##
##<!-- End Document Specific Declarations -->
##
##]>

##endsWithDoctype = re.compile(r'>$')
##print(endsWithDoctype.search(doctype))
##
##beginAndEndDoctype = re.compile(r'^<!DOCTYPE concept.*>$', re.DOTALL)
##print(beginAndEndDoctype.search(doctype))
# the following shows the entire doctype
beginAndEndDoctype2 = re.compile(r'^<!DOCTYPE concept.*>$', re.DOTALL)
print(beginAndEndDoctype2.findall(doctype2))
