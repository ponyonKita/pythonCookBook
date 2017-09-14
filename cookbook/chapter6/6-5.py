
# 딕셔너리를 xML로 바꾸기
from xml.etree.ElementTree import Element, tostring
from xml.sax.saxutils import escape, unescape

def dict_to_xml(tag, d):
    elem = Element(tag)
    for key, value in d.items():
        child = Element(key)
        child.text = str(value)
        elem.append(child)
    return elem


s = {
    'name':'GOOG',
    'shares':100,
    'price': 490.1,
    'tag':'<spam>'
}
e = dict_to_xml('stock', s)
e.set('_id', '1234')
print(tostring(e))

# 수동 이스케이핑
print(escape('<spam>'))
print(unescape('<spam>'))