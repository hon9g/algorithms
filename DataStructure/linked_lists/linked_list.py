"""
Singly Linked List

Time complexity:
  O(N) for get() addAtIndex() addAtTail() deleteAtIndex()
  O(1) for addAtHead()
  
Space complexity: O(N)
"""

class Node:
    def __init__(self, x: int, node: object = None):
        self.val = x
        self.next_node = node
        
        
class LinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = Node(-1)
        
    
    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        curr = self.head
        for _ in range(index):
            curr = curr.next_node
            if not curr:
                break
        return curr.val if curr else -1
        

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """  
        self.head = Node(val, self.head)

            
    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        if self.head.next_node:
            curr = self.head
            while curr.next_node.val != -1:
                curr = curr.next_node
            curr.next_node = Node(val, Node(-1))
        else:
            self.head = Node(val, Node(-1))
            
            
    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list.
        If index equals to the length of linked list, the node will be appended to the end of linked list.
        If index is greater than the length, the node will not be inserted.
        """
        if index == 0:
            self.addAtHead(val)
            return
        curr = self.head
        for _ in range(index - 1):
            curr = curr.next_node
        curr.next_node = Node(val, curr.next_node)
        

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        curr = self.head
        for _ in range(index):
            curr = curr.next_node
        if curr.val != -1:
            curr.val, curr.next_node = curr.next_node.val, curr.next_node.next_node
        
