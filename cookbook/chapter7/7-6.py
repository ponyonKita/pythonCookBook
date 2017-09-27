# 이름없는 함수와 인라인 함수 정의


add = lambda x, y:x+y

print(add(2,3))


names = ['a b', 'c d', 'b d', 'd c']

for name in names:
    print(name.split()[1])

print(sorted(names, key=lambda name:name.split()[-1].lower()))