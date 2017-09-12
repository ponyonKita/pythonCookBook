# 텍스트 검색과 치환

text = 'yarh, but no, but yeah, but no, but yeah'
print(text.replace('yeah', 'yep'))

text = 'Today is 11/27/2012. pycon starts 3/13/2013'
import re
print(re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text))

datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
print(datepat.sub(r'\3-\1-\2', text))


from calendar import month_abbr
def change_date(m):
    print('obv', m)
    mon_name = month_abbr[int(m.group(1))]
    print('m1', m.group(1))
    print('m2', m.group(2))
    print('m3', m.group(3))
    return '{} {} {}'.format(m.group(2), mon_name, m.group(3))

print(datepat.sub(change_date, text))

# 몇번 치환발생했는지 확인
nexttext, n = datepat.subn(r'\3-\1-\2', text)
print(nexttext)
print(n)