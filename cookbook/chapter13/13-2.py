

# 에러메세지와 함께 프로그램 종료


import sys
sys.stderr.write('It Fail')
raise SystemError(1)
# raise SystemError('It Fail') 로도 사용가능