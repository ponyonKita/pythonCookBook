# 텍스트 패턴 매칭과 검색

text = 'yeah, but no, but yeah, but no, but yeah'

print(text == 'yeah')

print(text.startswith('yeah'))
print(text.endswith('no'))
# 처음나타난곳 검색
print(text.find('no'))


import re

text = '11/27/2012'
text2 = 'Nov 27, 2012'

# \d+ = 하나이상의 숫자
if re.match(r'\d+/\d+/\d+', text):
    print('yes')

if re.match(r'\d+/\d+/\d+', text2):
    print('yes')
else:
    print('no')

# match는 항상 문자열 처음에만 찾기 시도
datepat = re.compile(r'\d+/\d+/\d+')
if datepat.match(text):
    print('yes')

# 텍스트 전체에 패턴을 찾을려면 findall

text3 = 'today is 2012/12/27. pycon starts 3/13/2013'
print(datepat.findall(text3))



# 캡쳐그룹 만들어서 사용하면 그룹을 개별적으로 추출할수 잇어 편함
# $ =  문자열의 마지막을 나타냄
datepat = re.compile(r'(\d+)(/\d+)(/\d+)$')
m = (datepat.match('11/27/2012'))
print(m.group(0))
print(m.group(1))
# 전체 매칭 찾기 (튜플로 생성됨)
print(datepat.findall(text3))

print('****')
# 한번에 결과를 얻지 않고 텍스트를 순환하며 찾음
for m in datepat.finditer(text3):
    print(m.group())