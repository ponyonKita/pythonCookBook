# 델리게이팅 순환


class Node:
    def __init__(self, value):
        self._value = value
        self._children = []

    def __repr__(self):
        return 'Node({value})'.format(value=self._value)

    def add_child(self, node):
        self._children.append(node)

    def __iter__(self):
        self.index = 0
        return iter(self._children)

    def __next__(self):
        if self.index >= len(self._children):
            #raise StopIteration
            pass
        n = self._children[self.index]
        self.index +=1
        return n

if __name__ == '__main__':
    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)
    root.add_child(child1)
    root.add_child(child2)
    print(type(root))

    for ch in root:
        print(ch)
        print(type(ch))

    root = iter(root)
    print(next(root))
    print(next(root))
    print(next(root))
