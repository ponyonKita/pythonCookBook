# 존재하지않는 파일에 쓰기


# xb = 바이너리 모

import os

if not os.path.exists('/Users/bhkim/pythonCookBook/cookbook'): # 검사할 파일 경로

    with open('/Users/bhkim/pythonCookBook/cookbook/somefile.txt', 'wt') as f:
        f. write('hello')
else:
    print('file already exists')