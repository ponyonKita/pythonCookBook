
# 구별자나 종단 부호 바꾸기

print('abc', 50, 91.5, sep=',')
print('abc', 50, 91.5, sep=',', end='!!\n')


for i in range(5):
    print(i, end=' ')


row = ('abc', 50, 91.5)
print(','.join(str(x) for x in row))
print(*row, sep='.')