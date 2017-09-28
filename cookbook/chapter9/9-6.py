# 옵션 매개 변수를 받는 데코레이터 정의


from functools import wraps, partial
import logging

def logged(func=None, *, level=logging.DEBUG, name=None, message=None):
    if func is None:
        return partial(logged, level=level, name=name, message=message)

    logname = name if name else func.__module__
    log = logging.getLogger(logname)
    logmsg = message if message else func.__name__

    @wraps(func)
    def wrapper(*args, **kwargs):
        log.log(level, logmsg)
        return func(*args, **kwargs)
    return wrapper

@logged(level=logging.CRITICAL, name='example')
def spam():
    print('Spam')


# a = spam()
# print(a)


@logged(level=logging.CRITICAL, name='example')
def add(x, y):
    return x+y

print(add(2,3))