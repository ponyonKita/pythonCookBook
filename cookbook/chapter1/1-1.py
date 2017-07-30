# 시퀀스를 개별 변수로 나누기


data = ['ACME', 50, 91.1, (2012,12,21)]
name, share, price, date = data

print(name)
print(date)

name, shares, price, (year, month, day) = data
print(name)
print(year)


s = 'hello'
a, b, c, d, e = s
print(a)


_, shares, price, _ = data
print(_)
print(price)