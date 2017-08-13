

#JSON데이터 읽고쓰기

import json

data = {
    'name': 'Selina',
    'shares': 100,
    'price': 542.33,
    'isSucceed': True,
    'isData': None
}

jsonData = json.dumps(data, indent=4, sort_keys=True)
print(jsonData)
data = json.loads(jsonData)
print(data)


data = '{"name": "Selina", "shares": "100", "price": 542.33, "isSucceed": "True", "isData": "null"}'

from collections import OrderedDict
data = json.loads(data, object_pairs_hook=OrderedDict)
print(data)


# json형식
with open('/Users/bhkim/pythonCookBook/cookbook/stock.txt', 'w') as f:
    json.dump(data, f)


# 파이썬형식
with open('/Users/bhkim/pythonCookBook/cookbook/stock.txt', 'r') as f:
    data = json.load(f)
    print(data)




class JSONObject:
    def __init__(self, d):
        self.__dict__ = d

s = '{"name": "Selina", "shares": "100", "price": 542.33, "isSucceed": "True", "isData": "null"}'
data = json.loads(s, object_hook=JSONObject)
print(data.name)


class Point:
    def __init__(self, x,y):
        self.x = x
        self.y = y

def serialize_instance(obj):
    d = {'__className__': type(obj).__name__}
    d.update(vars(obj))
    return d

#
# p = Point(2,3)
# print(json.dumps(p))


classes = {
    'Point':Point
}

def unserialize_object(d):
    clsName = d.pop('__classname__', None)
    if clsName:
        print('clsName', clsName)
        cls = classes[clsName]
        obj = cls.__new__(cls)
        for key, value in d.items():
            setattr(obj, key, value)
            return obj
    else:
        return d

p = Point(2,3)
s = json.dumps(p, default=serialize_instance)
print(s)

print(json.loads(unserialize_object(s)))
a = json.loads(s, object_hook=unserialize_object)
print(a)
