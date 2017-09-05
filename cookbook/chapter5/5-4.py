
# 바이너리 데이터 읽고 쓰릭
# 바이트 문자열 형식으로 출력됨
# with open('/Users/bhkim/pythonCookBook/cookbook/somefile.txt', 'rb') as f:
#     data = f.read(16)
#     text = data.decode('utf-8')
#
#     print(text)


# 바이트 문자열
b = b'hello world'
for c in b:
    print(c)

import array

nums = array.array('i', [1, 2, 3, 4])
with open('/Users/bhkim/pythonCookBook/cookbook/data.bin', 'wb') as f:
    f.write(nums)


a = array.array('i', [0, 0, 0, 0, 0, 0, 0, 0])
with open('/Users/bhkim/pythonCookBook/cookbook/data.bin', 'rb') as f:
    f.read(a)