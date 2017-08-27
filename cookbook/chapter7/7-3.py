

# 함수 인자에 메타데이터 넣기



def add(x:int, y:int) -> int:
    return x+y

print(add(2,3))

print(help(add))
print(add.__annotations__)