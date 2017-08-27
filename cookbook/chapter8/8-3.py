
# 객체의 콘텍스트 관리 프로토콜 지원
# 파일이나 네트워크 연결 락 등의 자원을 관리할때 일반적으로 사용
# 사용이 끝난 뒤에는 꼭 닫아야 데드락에 빠지지 않음

from socket import socket, AF_INET, SOCK_STREAM

class LazyConnection:
    def __init__(self, address, family=AF_INET, type=SOCK_STREAM):
        self.address = address
        self.family = AF_INET
        self.type = SOCK_STREAM
        #self.sock = None
        self.connections = []

    def __enter__(self):
        # if self.sock is not None:
        #     raise RuntimeError('Already connected')

        sock = socket(self.family, self.type)
        sock.connect(self.address)
        self.connections.append(sock)
        return sock

    def __exit__(self, exc_type, exc_val, exc_tb):
        #self.sock.close()
        #self.sock = None
        self.connections.pop().close()

from functools import partial

conn = LazyConnection(('www.python.org', 80))

with conn as s1:
    # conn.__enter__ 실행 연결
    s1.send(b'GET /index.html HTTP/1.0 \r\n')
    s1.send(b'Host: www.python.org\r\n')
    s1.send(b'\r\n')
    response = b''.join(iter(partial(s1.recv, 8192), b''))
    print(response)
    # conn.__exit__ 실행 연결종료
    with conn as s2:
        # conn.__enter__ 실행 연결
        s2.send(b'GET /index.html HTTP/1.0 \r\n')
        s2.send(b'Host: www.python.org\r\n')
        s2.send(b'\r\n')
        response2 = b''.join(iter(partial(s2.recv, 8192), b''))
        print(response2)
        # conn.__exit__ 실행 연결종료


# 아래와같은 출력값 노출됨
'''
b'HTTP/1.1 301 Moved Permanently\r\nServer: Varnish\r\nRetry-After: 0\r\nLocation: https://www.python.org/index.html
\r\nContent-Length: 0\r\nAccept-Ranges: bytes\r\nDate: Sun, 27 Aug 2017 14:31:52 GMT\r\nVia: 1.1 varnish
\r\nConnection: close\r\nX-Served-By: cache-nrt6130-NRT\r\nX-Cache: HIT\r\nX-Cache-Hits: 0
\r\nX-Timer: S1503844313.859813,VS0,VE0\r\nStrict-Transport-Security: max-age=63072000; includeSubDomains\r\n\r\n'
'''
