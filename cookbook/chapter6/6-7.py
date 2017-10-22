# 네임스페이스로 XML문서 파싱

from xml.etree.ElementTree import iterparse

for evt, elem in iterparse('ns2.xml', 'start-us', 'end-us'):
    print(evt, elem)