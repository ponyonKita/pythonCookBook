
# 여러구분자로 문자열 나누기



import re

line = 'asdf fjdk; afed, fjek,asdf,      foo'
print(re.split(r'[;,\s]\s*', line))

fields = re.split(r'(;|,|\s)\s*', line)
print('fields', fields)


values = fields[::2] # 홀수번쨰 아이템
print('values', values)
print(fields[1::2])
delimiters = fields[1::2] + ['']
print('delimiters', delimiters)


L= [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

print(L[1::2])
print(L[::2])