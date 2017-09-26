# 문자 입출력 작업 -:> 파일처럼 흉내내는 객체

import io
from io import StringIO

s = io.StringIO('helow')
s.write('hello world\n')
print('This is a test', file=s)
print(s.getvalue())

s = io.StringIO('hellow \n wolrd \n')
print(s.read(4))
print(s.read())