# UDP서버 생성


from socketserver import BaseRequestHandler,UDPServer
import time

class TimeHandler(BaseRequestHandler):
    def handle(self):
        print('Got connection from', self.client_address)
        msg, sock = self.request
        resp = time.ctime()
        sock.sendto(resp.encode('ascii'), self.client_address)

if __name__ == '__main__':
    serv = UDPServer(('', 20000), TimeHandler)
    serv.serve_forever()




# 메인 실행시키고 콘솔로 실행

# from socket import socket, AF_INET, SOCK_DGRAM
#
# s = socket(AF_INET, SOCK_DGRAM)
# s.sendto(b'', ('localhost', 20000))
#
# s.recvfrom(8192)


# 단일 스레드 이기때문에 동시에 요청을 하나만 보낼수있음
# 동시처리 위해서는 아래의 코드 필요

from socketserver import ThreadingUDPServer
...
if __name__ == '__main__':
    serv = ThreadingUDPServer(('',20000), TimeHandler)
    serv.serve_forever()


from socket import socket, AF_INET, SOCK_DGRAM
import time

def time_server(address):
    sock = socket(AF_INET, SOCK_DGRAM)
    sock.bind(address)
    while True:
        msg, addr = sock.recvfrom(8192)
        print('Got message from', addr)
        resp = time.ctime()
        sock.sendto(resp.encode('ascii'), addr)

if __name__ == '__main__':
    time_server(('', 20000))
