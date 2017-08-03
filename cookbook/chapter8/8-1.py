# 인스턴스의 문자열 표현식 변경



class Pair:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # 인스턴스 코드 표현식 반환(인스턴스를 재생성할때 입력하는 텍스트)
    # 인터프리터에서 값을 조사할때와 마찬가지로 이 텍스트 반환
    def __repr__(self):
        #return 'Pair({0.x!r}, {0.y!r})'.format(self)
        return 'Pair(%s, %s)'% (self.x, self.y)

    # 인스턴스를 문자열로 변환하고 str(), print()함수가 출력
    def __str__(self):
        return '({0.x!s}, {0.y!s})'.format(self)



p = Pair(3,4)
print(Pair(3,4))
print(p)

print('p is {0!r}'.format(p)) # !r 은 __repr__사
print('p is {0}'.format(p))