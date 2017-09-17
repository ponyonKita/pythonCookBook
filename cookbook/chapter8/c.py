# 클래스 이름의 캡슐호ㅏ
from cookbook.chapter8.b import B
class C(B):
    def __init__(self):
        super().__init__()
        self.__private = 1

    def __private_method(self):
        return 1

    def public_method(self):
        return 1

    def _internal_method(self):
        return 2

