
# 키워드 매개변수만 받는 함수 작성



def recv(maxsize, *, block):
    'Receives a message'
    pass


#print(recv(1024, True)) # type Error
print(recv(1024, block=True))



def mininum(*values, clip=None):
    m = min(values)
    if clip is not None:
        m = clip if clip > m else m
    return m

print(mininum(1, 5, 2, -5, 10))
print(mininum(1, 5, 2, -5, -1, clip=0))

print(help(recv))
print(help(mininum))