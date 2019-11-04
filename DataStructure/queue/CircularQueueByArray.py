"""
A circular queue by fixed size array

Time complexity: O(1) for all methods
Space complexity: O(k)
"""

class CircularQueueByArray:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.queue = [None] * k
        self.head, self.tail, self.k = -1, -1, k

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        elif self.isEmpty():
            self.head = self.tail = 0
        else:
            self.tail = (self.tail + 1) % self.k
        self.queue[self.tail] = value
        return True
        

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        elif self.head == self.tail:
            self.head = self.tail = -1
        else:
            self.head = (self.head + 1) % self.k
        return True
        

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        return self.queue[self.head] if not self.isEmpty() else -1
        

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        return self.queue[self.tail] if not self.isEmpty() else -1
    

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return self.head == -1
        

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return (self.head - 1) % self.k == self.tail % self.k
