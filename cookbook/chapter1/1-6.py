

# 딕셔너리 키를 여러값에 매핑하기

from collections import defaultdict
d = {
    'a':[1,2,3],
    'b':[4,5]
}
e = {
    'a':[6,7,8],
    'b':[9,10]
}


d = defaultdict(list)
d['a'].append(4)
d['a'].append(5)
d['b'].append(6)
print(d)

d = defaultdict(set)
d['a'].add(1)
d['a'].add(2)
d['b'].add(4)

print(d)

d = {}
d.setdefault('a',[]).append(1)
d.setdefault('a',[]).append(2)
d.setdefault('b',[]).append(4)

pairs = [{
    'a':1,
    'h': 1}]


d = defaultdict(list)
for key, value in pairs:
    print(key)
    print(value)
    d[key].append(value)

print(d)