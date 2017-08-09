

# 문자열 처음이나 마지막에 텍스트 매칭

fileName = 'spam.txt'
print(fileName.endswith('txt'))

print(fileName.startswith('sp'))

import os
fileName = os.listdir('.')
print(fileName)
test = [name for name in fileName if name.endswith(('.py', '.h'))]
print(test)
test2 = any(name.endswith('py') for name in fileName)
print(test2)


choices =['http:', 'ftp:']
url = 'http://www.python.org'
url.startswith(tuple(choices))

# 특정 디렉토리에 특정파일이있는지 확인
if any(name.endswith(('ppp')) for name in os.listdir('.')):
    print('dd')