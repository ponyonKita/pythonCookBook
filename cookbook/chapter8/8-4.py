

# 인스턴스를 많이 생성할때 메모리 절약
# 슬롯을 사용하면 인스턴스에서 훨씬 더 압축되 내부 표현을 사용
# 인스턴스 마다 딕셔너리를 구성하지 않고 튜플이나 리스트 같은 부피가 작은 고저 배열로 특정 인덱스에 매핑
# 부작용은 인스턴스에 새로운 속성을 추가 할수 없다는 점, 나열 한것만 사용가능함

class Date:
    __slots__ = ['year', 'month', 'day']
    print(type(__slots__))
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day


c = Date('12', '1', '3')
print(c.year)
print(c)