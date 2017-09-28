# 모듈 리로드
#import imp
#imp.reload()


def bar():
    print('bar')


def grok():
    print('Grok')


'''

import test
from cookbook.chapter10 import test
test.bar()
bar
test.grok()
Grok


import imp
imp.reload(test)
<module 'cookbook.chapter10.test' from '/Users/bhkim/pythonCookBook/cookbook/chapter10/test.py'>
test.bar()
bar
test.grok()
Grok TEst

'''