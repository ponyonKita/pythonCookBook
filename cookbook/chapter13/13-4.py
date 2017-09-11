# 암호 입력받기

import getpass


def svc_login(user, passwd):
    if user == 'test' and passwd == 'test':
        return True
    else:
        return False

user = getpass.getuser()
password = getpass.getpass()


if svc_login('test', password):
    print('Yah')
else:
    print('Boo')


