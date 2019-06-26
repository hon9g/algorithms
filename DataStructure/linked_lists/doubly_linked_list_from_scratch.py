"""
Doubly Linked List Implementation
"""
from typing import Union


class MyNode:
    def __init__(self, data: Union[int, float, str], prev_node=None, next_node=None) -> None:
        self.data = data
        self.prev_node = prev_node
        self.next_node = next_node

    def __str__(self) -> str:
        return str(self.data)


class DoublyLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def __len__(self) -> int:
        cnt: int = 0
        current = self.head
        while current:
            cnt += 1
            current = current.next_node
        return cnt

    def __str__(self) -> str:
        current = self.head
        y: str = str(current.data) + "->"
        while current.next_node:
            current = current.next_node
            y += str(current.data) + "->"
        y += "NULL"
        return y

    def append(self, x: Union[int, float, str]) -> None:
        if self.tail:
            self.tail.next_node = MyNode(x, prev_node=self.tail)
            self.tail = self.tail.next_node
            if not self.head.next_node:
                self.head.next_node = self.tail
                self.tail.prev_node = self.head
        else:
            self.head = self.tail = MyNode(x)

    def appendleft(self, x: Union[int, float, str]) -> None:
        if self.head:
            self.head.prev_node = MyNode(x, next_node=self.head)
            self.head = self.head.prev_node
            if not self.tail.prev_node:
                self.tail.prev_node = self.head
                self.head.next_node = self.tail
        else:
            self.head = self.tail = MyNode(x)

    def clear(self) -> None:
        current = self.head
        while current:
            current_next = current.next_node
            del current.next_node
            del current.prev_node
            current = current_next
        self.head = None
        self.tail = None

    def count(self, x: Union[int, float, str]) -> int:
        current = self.head
        cnt: int = 0
        while current:
            if current.data == x:
                cnt += 1
            current = current.next_node
        return cnt

    def insert(self, i: int, x: Union[int, float, str]) -> None:
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
                current.prev_node = MyNode(
                    x, prev_node=current.prev_node, next_node=current
                )

    def pop(self) -> Union[int, float, str]:
        if not self.head:
            raise IndexError
        y = self.tail
        if self.tail.prev_node:
            self.tail = self.tail.prev_node
            self.tail.next_node = None
        else:
            self.head = self.tail = None
        return y.data

    def popleft(self) -> Union[int, float, str]:
        if not self.head:
            raise IndexError
        y = self.head
        if self.head.next_node:
            self.head = self.head.next_node
            self.head.prev_node = None
        else:
            self.head = self.tail = None
        return y.data

    def remove(self, x: Union[int, float, str]):
        current = self.head
        while current:
            if current.data == x:
                p, n = current.prev_node, current.next_node
                p.next_node, n.prev_node = n, p
                break
            current = current.next_node
        else:
            raise ValueError

    def reverse(self) -> None:
        self.tail = current = self.head
        while current:
            n, current.next_node = current.next_node, current.prev_node
            p, current = current, n
        self.head = p
        return None

    def rotate(self, n: int) -> None:
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
