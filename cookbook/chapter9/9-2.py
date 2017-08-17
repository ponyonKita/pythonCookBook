
# 데코레이터 작성시 함수 메타데이터 보존


import time
from functools import wraps

def timethis(func):
    '''실행시간을 보고하는 데코레이터'''

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end-start)
        return result

    return wrapper

@timethis
def countdown(n:int):
    '''
    Count down
    '''
    while n > 0:
        n -= 1


countdown(10000)
print(countdown.__doc__)
print(countdown.__annotations__)

print(countdown.__wrapped__(100000))


from inspect import signature
print(signature(countdown))