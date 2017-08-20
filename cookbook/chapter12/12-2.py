
# 스레드가 시작되었는지 판단하기
#
# from threading import Thread, Event
import time
#
# def countdown(n, starts_evt):
#     print('countdown starting')
#     starts_evt.set()
#     while n > 0:
#         print('t-minus', n)
#         n -= 1
#         time.sleep(5)
#
#
# started_evt = Event()
#
# print('Launching countdown')
# t = Thread(target=countdown, args=(10, started_evt))
# t.start()
#
# started_evt.wait()
# print('countdown is running')
#


# 다른 스레드의 타이머가 만료되지 않았는지 지속적으로 확인
# event는 모든 스레드를 깨움

import threading
class PeriodicTimer:
    def __init__(self, interval):
        self._interval = interval
        self._flag = 0
        self._cv = threading.Condition()


    def start(self):
        t = threading.Thread(target=self.run)
        t.daemon = True
        t.start()

    def run(self):
        '''타이머를 실행하고 구간마다 기다리는 스레드에게 알림'''
        while True:
            time.sleep(self._interval)
            with self._cv:
                self._flag ^= 1
                self._cv.notify_all()

    def wait_for_tick(self):
        '''타이머의 타음 틱을 기다림'''
        with self._cv:
            last_flag = self._flag
            while last_flag == self._flag:
                self._cv.wait()

ptimer = PeriodicTimer(5)
ptimer.start()


def countdown(nticks):
    while nticks > 0:
        ptimer.wait_for_tick()
        print('t-minus', nticks)
        nticks -= 1


def countup(last):
    n = 0
    while n < last:
        ptimer.wait_for_tick()
        print('Counting', n)
        n += 1

threading.Thread(target=countdown, args=(10, )).start()
threading.Thread(target=countup, args=(5, )).start()

# 모든 스레드 안깨울려면

def worker(n, sema):
    sema.acquire()
    print('working', n)

sema = threading.Semaphore(0)
nworkers = 10
for n in range(nworkers):
    t = threading.Thread(target=worker, args=(n, sema, ))
    t.start()


sema.release()
