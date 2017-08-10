
# 정확한 10진수 계산

a = 4.2
b = 2.1
print(a+b)

print((a+b) == 6.3)

from decimal import Decimal, localcontext
a = Decimal('4.2')
b = Decimal('2.1')

print(a+b)
print((a+b) == Decimal('6.3'))

a = Decimal('1.3')
b = Decimal('1.7')
print(a/b)

with localcontext() as ctx:
    ctx.prec = 3     # 반올림자리수
    print(a/b)