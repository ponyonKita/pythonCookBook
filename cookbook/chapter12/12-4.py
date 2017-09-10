# 임계영역 락


# 임계영역이란 기본적으로 다중 프로세스 환경에서 나오는 개념이다.
# 서로 다른 둘 이상의 프로세스가 하나의 데이터 영역을 공유하고 있을 때 이 영역을 임계영역이라고 한다.
# 한마디로 문제가 발생할 만한 소지가 있는 위험하고도 중요한 영역이라는 말이다.

import urllib.request
import threading

class SharedCounter:
    '''다중 스레드에서 공유 가능한 카운터 객체'''

    _lock = threading.RLock()
    def __init__(self, initial_value=0):
        self._value = initial_value
        self._value_lock = threading.Lock()

    def incr(self, delta=1):
        '''락과 함께 카운터 증가'''
        with SharedCounter._lock:
            self._value +=delta

        # with self._value_lock:
        #     self._value += delta
        #     self._value_lock.release()

    def decr(self, delta=1):
        '''락과 함께 카운터 감소'''
        with SharedCounter._lock:
            self._value -= delta
        # with self._value_lock:
        #     self._value -= delta
        #     self._value_lock.release()




'''
상호배제란 위에서 설명한 임계영역을 보호하기 위한 개념이다.
즉 임계영역으로 인하여 발생할 수 있는 문제를 사전에 방지한다는 것이다.
임계영역으로 인하여 발생할 수 있는 문제는 둘 이상의 프로세스들이 공유자원을 동시에 읽거나 쓸때 발생한다.
그러므로 임계영역으로 인하여 발생할 수 있는 문제를 사전에 방지한다는 것은 둘 이상의 프로세스들이 공유자원
에 대해서 동시에 읽거나 쓰기를 못하게 하는 것이며 이것이 상호배제의 기본 개념이다.

그럼 상호배제를 다시 한번 정의해보자.

상호배제란 한 프로세스가 공유 메모리 혹은 공유자원을 사용하고 있을 때 다른 프로세스들은 이 메모리 혹은 자원을
사용하지 못하게 배제시키는 제어 기법을 말한다.

이를 위해서 특정 프로세스는 공유 메모리 혹은 공유자원을 사용하기 전에 먼저 이렇게 선언한다.
"자! 지금 부터 이 공유메모리는 내가 사용을 할때니까 아무도 접근하지마!"
그리고 공유자원에 대해서 모든 사용이 끝나면
"자! 나는 사용이 끝났으니까 이제  사용해도되!"
라고 말하는 형식이다.

즉 운영체제는 둘 이상의 프로세스가 동시에 임계영역에 들어 갈수 없도록 수행순서를 잘 조절하는 역할을 한다.
'''



