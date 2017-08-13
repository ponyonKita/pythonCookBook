


# 파일에 출력
# with open('/Users/bhkim/pythonCookBook/cookbook/stock.txt', 'wt') as f:
#     f.write('hello')
#


with open('/Users/bhkim/pythonCookBook/cookbook/stock.txt', 'w') as f:
    print('HELLO WORLD', file=f)