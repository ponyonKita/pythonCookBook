

# 매개변수 개수에 구해받지 않는 함수 작성



# 위치 매개변수에 개수 제한이 없는 함수  -> *
def avg(first, *rest):
    return (first + sum(rest) / (1+len(rest)))

print(avg(1,2))
print(avg(1,2,3,4))

# 키워드 매개변수 수에 제한이 없는 함수 작성 -> **

import html

def make_element(name, value, **attrs):
    keyvals = [' %s="%s"' % item for item in attrs.items()]
    print(keyvals)
    attr_str = ''.join(keyvals)

    element = '<{name}{attrs} > {value} </{name}>'.format(name=name, attrs=attr_str, value=html.escape(value))

    return element


print(make_element('item', 'Albatross', size='large', quantity=6))
print(make_element('p', '<spam>'))


def anyargs(*args, **kwargs):
    print(args) # 튜플
    print(kwargs) # 딕셔너

print(anyargs('f', 'j', test=1, type=2, list=3))


# *는 함수정의의 마지막 위치 매개변수 자리에만 올수있다
# ** 는 마지막 매개변수 자리에만 올수있다
def a(x, *args, y):
    pass

def b(x, *args, y, **kwargs):
    pass