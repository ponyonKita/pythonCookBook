# 우선순위 큐 구현
import heapq

class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]


class Item:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'Item(%s)' %self.name


q = PriorityQueue()
q.push(Item('foo'), 1)
q.push(Item('bar'), 5)
q.push(Item('spam'), 4)
q.push(Item('grock'), 1)

print(q.pop())
print(q.pop())
print(q.pop())
print(q.pop())

# poiority, index, item
a = (1, 0,Item('foo'))
b = (5, 1,Item('bar'))
print(a>b)