
# csv데이터 읽고쓰기

import csv
#
# # row가 리스트형태로 나옴
with open('/Users/bhkim/pythonCookBook/cookbook/stock.txt') as f:
    f_csv = csv.reader(f)
    headers = next(f_csv)
    for row in f_csv:
        print(row)
# --> ['1', '2', '3', '4', '5']
#
# # 인덱스 사용에 헷갈려서 네임드튜플사용
#
# from collections import namedtuple
#
# with open('/Users/bhkim/pythonCookBook/cookbook/stock.txt') as f:
#     f_csv = csv.reader(f)
#     headings = next(f_csv)
#     rows = namedtuple('Row', headings)
#     for r in f_csv:
#         row = rows(*r)
#         print(row)
# --> Row(a='1', b='2', c='3', d='4', f='5')
#
#
# # 딕셔너리 시퀀스로 읽기
#
# with open('/Users/bhkim/pythonCookBook/cookbook/stock.txt') as f:
#     f_csv = csv.DictReader(f)
#     for row in f_csv:
#         print(row)
# --> OrderedDict([('a', '1'), ('b', '2'), ('c', '3'), ('d', '4'), ('f', '5')])

# 튜플형식으로 된 값 쓰기
headerString = ['a','b', 'c', 'd', 'e']
# rowsTuple = [('1', '2', '3', '4', '5'), ('1', '2', '3', '4', '5')]
# with open('/Users/bhkim/pythonCookBook/cookbook/stock.txt', 'w') as f:
#     f_csv = csv.writer(f)
#     f_csv.writerow(headerString)
#     f_csv.writerows(rowsTuple)

#
# # 딕셔너리 형식 값 쓰기
# rows = [{'a':'1', 'b':'2', 'c':'3', 'd':'4', 'e':'5'}, {'a':'1', 'b':'2', 'c':'3', 'd':'4', 'e':'5'}]
# with open('/Users/bhkim/pythonCookBook/cookbook/stock.csv', 'w') as f:
#     f_csv = csv.DictWriter(f, headerString)
#     f_csv.writeheader()
#     f_csv.writerows(rows)


#