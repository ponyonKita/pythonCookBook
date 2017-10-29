x = 10
a  = lambda y:x+y


x = 20
b = lambda y:x+y

print(a(10))
print(b(10))

x = 15
print(a(10))


# 고정값 사용
x = 10
a = lambda y, x=x:x+y
print(a(10))

x = 20
b = lambda y, x=x:x+y
print(b(10))


func = [lambda x:x+n for n in range(5)]
for f in func:
    print(f(0))

# 올바른 표현식
func = [lambda x, n=n:x+n for n in range(5)]
for f in func:
    print(f(0))