
# 스레드간 통신

# 큐의 현재크기 -> q.qsize(), q.full(), q.empty() -> 호출한 순간 다른 스레드가 큐에 아이템 추가한경우
# 정확하지 않을수있다.
from queue import Queue
from threading import Thread, Event
import copy

_sentinel = object()

def product(out_q):
    while True:
        # 데이터생성
        data = 3
        evt = Event()
        # 큐에 아이템을 넣을때 복사본이 생기지 않아서 스레드간 통신할때는 실제로 객체를 주고받는다
        # 공유 상태가 걱정이 된다면 깊은 복사 필요
        out_q.put(copy.deepcopy(data, evt), block=False)
        evt.wait()
    #out_q.put(_sentinel)

#데이터 소비 쓰레드
def consumer(in_q):
    while True:
        # 데이터얻기
        data, evt = in_q.get(timeout=5.0)
        # 종료알림
        evt.set()
        # # 종료확인
        # if data is _sentinel:
        #     in_q.put(_sentinel)
        #     break

        # 데이터 처리


q = Queue()
t1 = Thread(target=consumer, args=(q,))
t2 = Thread(target=product, args=(q,))

t1.start()
t2.start()
print(t1)
# 생성된 모든 아이템을 소비할때까지 기다림(기본적인 종료)
q.join()

##########################
# 단방향 비결정적 처리 -> 큐로 구현한 스레드통신

# 언제 메세지를 받았고 처리를 했는지 알수없다

import heapq
import threading

class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._count = 0
        self._cv = threading.Condition()

    def put(self, item, priority):
        with self._cv:
            heapq.heappush(self._queue, (-priority, self._count, item))
            self._count +=1
            self._cv.notify()

    def get(self):
        with self._cv:
            while len(self._queue) == 0:
                self._cv.wait()

        return heapq.heappop(self._queue)[-1]



