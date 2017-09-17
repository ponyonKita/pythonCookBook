# 클래스 이름의 캡슐호ㅏ

class B:
    def __init__(self):
        self.__private = 0

    def __private_method(self):
        return 1

    def public_method(self):
        return 1

    def _internal_method(self):
        return 2

