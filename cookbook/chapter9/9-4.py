

# 매개변수를 받는 데코레이터 정의

from functools import wraps
import logging

def logged(level, name=None, message=None):
    def decorate(func):
        logname = name if name else func.__module__
        log = logging.getLogger(logname)
        logmsg = message if message else func.__name__

        @wraps(func)
        def wrapper(*args, **kwargs):
            log.log(level, logmsg)
            return func(*args, **kwargs)
        return wrapper
    return decorate



@logged(logging.DEBUG)
def add(x,y):
    return x+y

@logged(logging.CRITICAL, 'example')
def spam():
    print('Spam!')

print(spam())
print(add(1,2))


logging.debug("디버깅용 로그~~")
logging.info("도움이 되는 정보를 남겨요~")
logging.warning("주의해야되는곳!")
logging.error("에러!!!")
logging.critical("심각한 에러!!")


@decorator(x, y, z)
def func(a,b):
    pass



def func(a,b):
    pass

func = decorate(x,y,z)(func)