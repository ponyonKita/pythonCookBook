# 파일 입출력 텍스트 데이터 읽고 쓰기



# 파일전체 하나의 문자열로 읽음
with open('/Users/bhkim/pythonCookBook/cookbook/somefile.txt', 'rt') as f:
    data = f.read()
    print(data)


f = open('/Users/bhkim/pythonCookBook/cookbook/somefile.txt', 'rt')
print(f.read())
f.close()

# newline : 줄바꿈변환 미사용(윈도우형식으로 인코딩된 텍스트 파일을 읽어올때 모든줄바꿈문자를 \n으로 변환해서 무시할때 사용
# errors :  인코딩이 다를때 처리방법 ignore -> 무시 replace -> 바꿈
f = open('/Users/bhkim/pythonCookBook/cookbook/somefile.txt', 'rt', newline='', encoding='ascii', errors='ignore')
print(f.read())
f.close()