
# 정규식 숫자만 추출하기, 문자만 추출하기

import re


testString = 'abc124abc12abd'

numberMatch = re.compile(r'[0-9]\d*')
print(numberMatch.findall(testString))


stringMatch = re.compile(r'[a-zA-Z]\D*')
print(stringMatch.findall(testString))