

# 이터레이터 언패킹

test = [1,2,3]

def iterater(n):
    for x in iter(n):
        print(x)

a,b,c = iter(test)
print(a)
print(b)
print(c)

print(iterater(test))

# 제너레이터 언패킹

def generator(n):
    for x in range(n):
        yield x

result = generator(10)
print(list(result))



