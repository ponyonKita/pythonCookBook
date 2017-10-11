
# 딕셔너리 순서유지
from collections import OrderedDict

d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
d['grok'] = 4


print(d)

import ujson

print(ujson.dumps(d))