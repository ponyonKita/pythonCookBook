#쓰레디 시작과 정지


import time
def countdown(n):
    while n > 0 :
        print('T-minus', n)
        n -= 1
        time.sleep(5)


from threading import Thread

t = Thread(target=countdown, args=(10,), daemon=True)
t.start()
t.join(20) # 실제종료까지 기다림(필요한경우)

# 쓰레드 실행중 여부
if t.is_alive():
    print('running')
else:
    print('stop')