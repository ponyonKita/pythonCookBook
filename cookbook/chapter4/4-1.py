# 수동으로 이터레이터 소비



with open('etc/passwd') as f:
    while True:
        line = next(f, None)
        if line is None:
            break
        print(line, end='')



# 대게의 경우에 순환을 사용하는데 더 정교한 조절이 필요할때 ????


