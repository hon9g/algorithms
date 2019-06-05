"""
Doubly Linked List Implementation
"""


class Node:
    def __init__(self, data: str, prev_node=None, next_node=None) -> None:
        self.data: str = data
        self.prev_node: Node = prev_node
        self.next_node: Node = next_node

    def __str__(self):
        return str(self.data)


class DoublyLinkedList:
    def __init__(self) -> None:
        self.head: Node = None
        self.tail: Node = None

    def __len__(self):
        cnt: int = 0
        current: Node = self.head
        while current:
            cnt += 1
            current = current.next_node
        return cnt

    def __str__(self):
        current: Node = self.head
        y: str = ""
        while current:
            y += str(current) + "->"
            current = current.next_node
        y += "NULL"
        return y

    def append(self, x):
        if self.tail:
            self.tail.next_node: Node = Node(x, prev_node=self.tail)
            self.tail = self.tail.next_node
        else:
            self.head = self.tail = Node(x)

    def appendleft(self, x):
        if self.head:
            self.head.prev_node: Node = Node(x, next_node=self.head)
            self.head = self.head.prev_node
        else:
            self.head = self.tail = Node(x)

    def clear(self):
        self.head = None
        self.tail = None

    def count(self, x):
        current_node: Node = self.head
        cnt: int = 0
        while current_node:
            if current_node.data == x:
                cnt += 1
            current_node = current_node.next_node
        return cnt

    def insert(self, i, x):
        if i == 0:
            self.appendleft(x)
        elif i == -1:
            self.append(x)
        else:
            current = self.head
            for _ in range(i):
                current = current.next_node
            if current is None:
                self.append(x)
            else:
                current.prev_node = Node(
                    x, prev_node=current.prev_node, next_node=current
                )

    def pop(self):
        if not self.tail:
            raise IndexError
        y: Node = self.tail
        if self.tail.prev_node:
            self.tail = self.tail.prev_node
            self.tail.next_node = None
        else:
            self.head = self.tail = None
        return y.data

    def popleft(self):
        if not self.head:
            raise IndexError
        y = self.head
        if self.head.next_node:
            self.head = self.head.next_node
            self.head.prev_node = None
        else:
            self.head = self.tail = Node
        return y.data

    def remove(self, x):
        current: Node = self.head
        while current:
            if current.data == x:
                p, n = current.prev_node, current.next_node
                p.next_node, n.prev_node = n, p
                break
            current = current.next_node
        else:
            raise ValueError

    def reverse(self):
        self.tail = current = self.head
        while current:
            n, current.next_node = current.next_node, current.prev_node
            p, current = current, n
        self.head = p
        return None

    def rotate(self, n: int):
        if self.head:
            if 0 < n:
                for _ in range(n):
                    x = self.pop()
                    self.appendleft(x)
            elif n < 0:
                for _ in range(n * -1):
                    x = self.popleft()
                    self.append(x)
        else:
            raise IndexError
