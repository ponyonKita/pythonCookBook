

# 쉘 와일드 카드 패턴으로 문자열 매칭

# 맥에서는 대소문자 구분 윈도우에서는 구분하지않음
# 이런 운영체제에 따라 대소문자 구분하는게 싫으면 fnmatchcas쓰면됨(철저하게 대소문자 구분)

# 파일이름을 찾는 함수가 필요하면 glob모듈 사용하는게 좋음


from fnmatch import fnmatch, fnmatchcase
print(fnmatch('foo.txt', '?oo.txt'))
print(fnmatch('Dat45.csv', 'Dat[0-9]*'))

names = ['Dat1.csv', 'Dat2.csv', 'config.ini', 'foo.py']
print([name for name in names if fnmatch(name, 'Dat*.csv')])

print(fnmatchcase('test.csv', '*.csv'))


addresses = [
    '5412 N CLARK ST',
    '1060 W ADDISON ST',
    '1039 W GRANVILLE AVE',
    '2122 N CLARK ST',
    '4802 N BROADWAY'
]

print([addr for addr in addresses if fnmatchcase(addr, '* ST') ])
print([addr for addr in addresses if fnmatchcase(addr, '54[0-9][0-9] *CLARK*') ])