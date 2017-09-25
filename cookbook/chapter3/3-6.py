# 복소수 계산


a = complex(2,4)
b = 3-5j
print(type(a))
print(type(b))

print(a.real) # 실수
print(a.imag) # 허수
print(a.conjugate()) # 켤레 복소수

print(a+b)
print(a*b)
print(a/b)
print(abs(a))

import cmath
print(cmath.sin(a))

# 복소수 배열 계산

import numpy as np

a = np.array([2 + 3j, 4+5j, 8+9j])
print(a)