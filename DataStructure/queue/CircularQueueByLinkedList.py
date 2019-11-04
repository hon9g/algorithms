"""
A circular queue by a linked list

Time complexity: O(1) for all methods
Space complexity: O(k) when the queue is full
"""

class Node:
    def __init__(self, x: int):
        self.val = x
        self.next = None


class CircularQueueByLinkedList:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.capacity, self.count = k, 0
        self.head = self.tail  = None

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        elif self.isEmpty():
            self.head = self.tail = Node(value)
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next
        self.count += 1
        return True
        

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        elif self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
        self.count -= 1
        return True
        

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        return self.head.val if not self.isEmpty() else -1
        

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        return self.tail.val if not self.isEmpty() else -1
    

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return self.count == 0
        

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return self.capacity <= self.count
