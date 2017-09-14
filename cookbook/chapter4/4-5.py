
# 역방향 순환

class CountDown:
    def __init__(self, start):
        self.start = start


    def __iter__(self):
        n = self.start
        while n > 0:
            yield n
            n -=1

    def __reversed__(self):
        n = 1
        while n <= self.start:
            yield n
            n += 1

d = CountDown(5)
for i in d.__iter__():
    print(i)
for i in d.__reversed__():
    print(i)

print(type(d))
print(d.start)
