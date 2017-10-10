# 외부 명령 실행하고 결과 얻기

import subprocess
'''
subprocess 모듈은 파이썬 프로그램 내에서 새로운 프로세스를 스폰하고 여기에 입출력 파이프를 연결하며 리턴코드를 획득할 수 있도록 하는 모듈로,
다른 언어로 만들어진 프로그램을 통합, 제어할 수 있게 만드는 모듈이다.
 이 모듈은 기존에 오랜된 몇몇 모듈과 함수(os.system, os.spawn*)들을 대체하기 위해 만들어졌다.
'''



# out_bytes = subprocess.check_output(['netstat', '-a'])
#
# #out_bytes = subprocess.check_output('grep python | wc > out' , shell=True)
# print(out_bytes)


text = b''' hello world this is a test goodbye'''

p = subprocess.Popen(['wc'], stdout=subprocess.PIPE, stdin=subprocess.PIPE)

stdout, stderr = p.communicate(text)

out = stdout.decode('utf-8')
err = stderr.decode('utf-8')

print(out)
print(err)