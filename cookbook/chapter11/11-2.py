
# TCP 서버만들기


from socketserver import BaseRequestHandler, TCPServer, StreamRequestHandler

class EchoHandler(BaseRequestHandler):
    def handle(self):
        print('Got connection from', self.client_address)
        while True:
            msg = self.request.recv(8192)
            if not msg:
                break
            self.request.send(msg)

        # StreamRequestHandler
        # for line in self.rfile:
        #     self.wfile.write(line)


if __name__ == '__main__':
    serv = TCPServer(('', 20000), EchoHandler)
    serv.serve_forever()

# 다중 클라이언트 서버

from socketserver import ThreadingTCPServer
import socket
if __name__ == '__main__':
    server = ThreadingTCPServer(('', 20000), EchoHandler)
    server.serve_forever()



#클라이언트 하나마다 새로운 프로세스나 스레드 만들어서 접속한다면 해커의 위험이 있어서
# 워커 스테드나 프로세스를 미리 할당한 풀만들면됨

if __name__ == '__main__':
    from threading import Thread
    NWORKERS = 16
    serv = TCPServer(('', 20000), EchoHandler)
    for n in range(NWORKERS):
        t = Thread(target=serv.serve_forever())
        t.daemon = True
        t.start()
    serv.serve_forever()

# 일반적으로 TCP서버는 인스턴스화 할때 기반 소켓을 묶고 활성화
# 옵션을 설정해서 소켓을 조절할려면
serv = TCPServer(('', 20000), EchoHandler, bind_and_activate=False)
serv.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)

# 위의 소켓옵션은 서버가 이미 사용한 포트번호에 다시 묶이도록 하는 일반적인 셋팅이라 TCPServer의 클래스 변수에서도 설정가능

TCPServer.allow_reuse_address = True
serv = TCPServer(('', 20000), EchoHandler)
serv.serve_forever()



# 콘솔로 실행

from socket import socket, AF_INET, SOCK_STREAM

s = socket(AF_INET, SOCK_STREAM)
s.connect(('localhost', 20000))
s.send(b'hello')
s.recv(8192)
