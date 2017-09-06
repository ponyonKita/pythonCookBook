# 함수에서 여러값을 반환

def myfun():
    return 1,2,3

a,b,c = myfun()
print(a)
x = myfun()
print(x)
print(type(x))

a = (1,2)
b = 1,2
print(type(a))