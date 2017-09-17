

# 기본인자를 사용하는 함수정의


_no_value = object()

def spam(a, b=_no_value):
    if b is _no_value:
        print('No b value supplied')

#s = spam(1)
print(spam(1))
_no_value = {'test':'test'}
print(spam(1,2))


# 할당하는 기본값은 함수를 정의할때 한번만 정해지고 그 이후에는 변하지않음
x = 42
def spam(a, b=x):
    print(a,b)

print(spam(1))
x = 41

print(spam(1))


# 기본값으로 사용하는 값은 None, True, False, 숫자, 문자열 같이 항상 변하지 않는 객체사용

def spam(a, b=[]):
    print(b)
    return b

x = spam(1)
print(x)
x.append(99)
x.append('ssss')
print(x)