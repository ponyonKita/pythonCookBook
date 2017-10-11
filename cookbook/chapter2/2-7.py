
# 가장 짧은 매칭을 위한 정규 표현식

import re
str_pat = re.compile(r'\"(.*)\"')
text = 'Computer says "no." Phone says "yes."'
print(str_pat.findall(text))

str_pat = re.compile(r'\"(.*?)\"')
text = 'Computer says "no." Phone says "yes."'
print(str_pat.findall(text))