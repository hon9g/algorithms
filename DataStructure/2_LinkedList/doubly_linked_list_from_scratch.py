"""
Doubly Linked List Implementation
"""

class Node:
    def __init__(self, data: str, prev_node = None, next_node = None) -> None:
        self.data: str = data
        self.prev_node: Node = prev_node
        self.next_node: Node = next_node

class DoublyLinkedList:
    def __init__(self) -> None:
        self.head: Node = None
        self.tail: Node = None
        self.size: int = 0

    def append(self, x):
        if self.tail:
            self.tail.next_node: Node = Node(x, prev_node=self.tail)
            self.tail = self.tail.next_node
        else:
            self.head = self.tail = Node(x)
        self.size += 1

    def appendleft(self, x):
        if self.head:
            self.head.prev_node: Node = Node(x, next_node=self.head)
            self.head = self.head.prev_node
        else:
            self.head = self.tail = Node(x)
        self.size += 1

    def clear(self):
        self.head = None
        self.tail = None
        self.size = 0

    def count(self, x):
        current_node: Node = self.head
        cnt: int = 0
        while current_node: # O(N)
            if current_node.data == x:
                cnt += 1
            current_node = current_node.next_node
        return cnt

    def index(self, x):
        return x

    def insert(self, i, x):
        if i == 0:
            self.appendleft(x)
        elif i == self.size-1:
            self.append(x)
        else:
            current_node = self.head
            for _ in range(i):
                current_node = current_node.next_node
            current_node.prev_node = Node(x, prev_node=current_node.prev_node, next_node=current_node)
        self.size += 1

    def pop(self):
        if not self.tail:
            raise IndexError
        y = self.tail
        if self.tail.prev_node:
            self.tail = self.tail.prev_node
            self.tail.next_node = None
        else:
            self.head = self.tail = None
        self.size += -1
        return y

    def popleft(self):
        if not self.head:
            raise IndexError
        y = self.head
        if self.head.next_node:
            self.head = self.head.next_node
            self.head.prev_node = None
        else:
            self.head = self.tail = Node
        self.size += -1
        return y

    def remove(self, x):
        self.size += -1
        current_node = self.head
        while current_node:
            if current_node.data == x:
                p, n = current_node.prev_node, current_node.next_node
                p.next_node, n.prev_node = n, p
                break
        else:
            raise ValueError

    def reverse(self):
        if 1 < self.size:
            self.head, self.tail = self.tail, self.head
            current_node = self.head
            while current_node:
                current_node.prev_node, current_node.next_node = current_node.next_node, current_node.prev_node
                current_node = current_node.next_node
        return None

    def rotate(self, n:int=1):
        if self.size < 1:
            if n < 0:
                for _ in range(n % self.size):
                    self.appendleft(self.pop())
            elif 0 < n:
                for _ in range((n*-1) % self.size):
                    self.append(self.popleft())