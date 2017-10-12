def count(n):
    while True:
        yield n
        n += 1


#
'''
 islice () 함수는 slice () 함수와 동일하게 작동합니다. 첫 번째 매개 변수는 반복 가능한 객체이고,
  두 번째 매개 변수는 시작 색인입니다. 세 번째 매개 변수는 끝 색인입니다.
  마지막 매개 변수는 각 반복 후에 건너 뛸 수있는 단계 또는 숫자입니다.

'''
c = count(0)
# print(c[10:20])

import itertools
for x in itertools.islice(c, 10, 20, 2):
    print(x)