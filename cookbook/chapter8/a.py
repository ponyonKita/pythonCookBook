# 클래스 이름의 캡슐호ㅏ 8-5

class A:
    def __init__(self):
        self._internal = 0
        self.public = 1

    def public_method(self):

        return 1

    def _internal_method(self):

        return 2

