# 마지막 N개 아이템 유지


from collections import deque


def search(lines, pattern, history=5):

    previous_line = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_line
            print('line', line)
            print('previous_line', previous_line)
        previous_line.append(line)
    return previous_line


if __name__ == '__main__':
    with open('/Users/bhkim/pythonCookBook/cookbook/somefile.txt') as f:
        for line, prevlines in search(f, 'python', 5):
            for pline in prevlines:
                print(pline, end='')
            print(line, end='')
            print('-'*20)




q = deque(maxlen=3)
q.append(1)
q.append(2)
q.append(3)
print(q)


q.append(4)
print(q)


# 크기 지정안함
test = deque()
test.append(1)
test.append(2)
test.append(3)

print(test)
test.appendleft(4)
print(test)
test.pop()
print(test)
test.popleft()
print(test)