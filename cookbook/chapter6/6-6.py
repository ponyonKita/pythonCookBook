'''

<?xml version="1.0"?>
<stop>
    <id>14791</id>
    <nm>Clark &amp; Balmoral</nm>
    <sri>
        <rt>22</rt>
        <d>North Bound</d>
        <dd>North Bound</dd>
    </sri>
    <cr>22</cr>
    <pre>
       <pt>5 MIN</pt>
       <fd>Howard</fd>
       <v>1378</v>
       <rn>22</rn>
   </pre>
   <pre>
       <pt>15 MIN</pt>
       <fd>Howard</fd>
       <v>1867</v>
       <rn>22</rn>
   </pre>
</stop>
'''

from xml.etree.ElementTree import parse, Element
doc = parse('pred.xml')
root = doc.getroot()
print(root)
# Remove a few elements
root.remove(root.find('sri'))
root.remove(root.find('cr'))

# Insert a new element after <nm>...</nm>
root.getchildren().index(root.find('nm'))

e = Element('spam')
e.text = 'This is a test'
root.insert(2, e)

# Write back to a file
doc.write('newpred.xml', xml_declaration=True)