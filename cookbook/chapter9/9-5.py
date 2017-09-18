from functools import wraps, partial
import logging

def attach_wapper(obj, func=None):
    if func is None:
        return partial(attach_wapper, obj)

def logged(level, name=None, message=None):
    '''함수에 로깅추가 level은 로깅 레벨, name은 로거이름, message는 로그메세지
    name과 message가 명시되어있지않으면 함수의 모듈 이름을 기본값으로 한다'''

    def decorate(func):
        logname = name if name else func.__module__
        log = logging.getLogger(logname)
        logmsg = message if message else func.__name__


        @wraps(func)
        def wrapper(*args, **kwargs):
            log.log(level, logmsg)
            return func(*args, **kwargs)

        @attach_wapper(wrapper)
        def set_level(newlevel):
            global level
            level = newlevel

        @attach_wapper(wrapper)
        def set_message(newmsg):
            global logmsg
            logmsg = newmsg


        return wrapper
    return decorate



@logged(logging.DEBUG)
def add(x,y):
    return x+y

@logged(logging.CRITICAL, 'example')
def spam():
    print('Spam!')

# global이랑 nonlocal이랑 다른가??

# 여러 속성바꿈
logging.basicConfig(level=logging.DEBUG)
print(add(2,3))
#
# add.set_message('Add called') # 이거작동안함
# print(add(2,3))

add.set_level(logging.WARNING) # 작동안함
print(add(2,3))