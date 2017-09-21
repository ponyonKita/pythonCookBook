# 터미널 크기 구하기

import os
sz = os.get_terminal_size()
print(sz)
print(sz.columns)

print(sz.lines)
