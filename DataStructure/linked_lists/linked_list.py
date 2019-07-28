"""
Simple Linked List
"""

class node:
    def __init__(self, x, nex=None):
        self.val = x
        self.next_node = nex
    def __str__(self):
        return str(self.val)

class linkedList:
    def __init__(self):
        self.head = None
    
    def createLinkedList(self, arr):
        if not arr:
            raise ValueError
        self.head = node(arr[0])
        curr = self.head
        for i in range(1, len(arr)):
            curr.next_node = node(arr[i])
            curr = curr.next_node
        return self.head
    
    def __str__(self):
        curr = self.head
        y = str(curr.val) + '->'
        while curr.next_node:
            curr = curr.next_node
            y += str(curr.val) + '->'
        y += 'NULL'
        return y
