# 일괄 임포트 제어
#
def spam():
    print('spam')
    return 2


def grok():
    print('grok')
    return 3

blah = 42

__all__ = ['spam', 'grok', 'test']


