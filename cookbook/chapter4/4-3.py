

# 제너레이터로 새로운 순환 패턴 샏성

def frange(start, stop, increment):
    x = start
    while x < stop:
        yield x
        x += increment


for n in frange(0, 4, 0.5):
    print(n)


print(list(frange(0, 1, 0.125)))


def countdown(n):
    print('Starting to count from', n)
    while n > 0:
        yield n
        n-=1
    print('Done')

c = countdown(3)
print(c)
print(next(c))
print(next(c))
print(next(c))
print(next(c))