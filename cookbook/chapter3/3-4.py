


# 2진수 8진수, 16진수 작업

# 2진수
x = 1234
print(bin(x))
print(format(x, 'b')) # 맨앞의 0b, 0o, 0x제거
#8진수
print(oct(x))
print(format(x, 'o'))
# 16진수
print(hex(x))
print(format(x, 'x'))

x = -1234
print(format(x, 'b'))
print(format(x, 'x'))
print(format(2**32 + x, 'b')) # 비트길이지정
print(format(2**32 + x, 'x'))

print(int('4b2', 16))
print(int('10011010010', 2))


import os
# 8진법앞에는 0o을 붙여야 오류가 안남
#print(os.chmod('script.py', 0755))
print(os.chmod('script.py', 0o755))