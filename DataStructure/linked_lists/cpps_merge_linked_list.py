"""
Problem solving during cpps study
topic: Linked List
problem: Merge Linked Lists in order from two ordered Linked Lists
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
    
    def create(self, arr):
        if not arr:
            raise ValueError
        self.head = node(arr[0])
        curr = self.head
        for i in range(1, len(arr)):
            curr.next_node = node(arr[i])
            curr = curr.next_node
        return self

    def popLeft(self):
        if not self.head:
            raise ValueError
        y = self.head.val
        self.head = self.head.next_node
        return y
    
    def __str__(self):
        curr = self.head
        y = str(curr.val) + '->'
        while curr.next_node:
            curr = curr.next_node
            y += str(curr.val) + '->'
        y += 'NULL'
        return y


class Solution:
    def mergeList(self, N, M):
        """
        Merge 2 sorted Linked Lists

        Time Complexity: O(N) if N > M
        Space Complexity: O(1)

        >>> N, M = linkedList().create([1, 2, 4]), linkedList().create([1, 3, 4])
        >>> print(N)
        1->2->4->NULL
        >>> print(M)
        1->3->4->NULL
        >>> f = Solution().mergeList
        >>> y = f(N,M)
        >>> print(y)
        1->1->2->3->4->4->NULL
        >>> print(M.create([1,2,3]))
        1->2->3->NULL
        >>> print(N.create([1,2,3]))
        1->2->3->NULL
        >>> y = f(N,M)
        >>> print(y)
        1->1->2->2->3->3->NULL
        >>> print(N.create([0,6,9]))
        0->6->9->NULL
        >>> print(M.create([1,2,3]))
        1->2->3->NULL
        >>> y = f(N,M)
        >>> print(y)
        0->1->2->3->6->9->NULL
        """

        result = linkedList()
        if N.head.val <= M.head.val:
            result.head = node(N.popLeft())
        else:
            result.head = node(M.popLeft())
        
        curr = result.head

        while N.head and M.head:
            if N.head.val <= M.head.val:
                x = N.popLeft()
            else:
                x = M.popLeft()
            curr.next_node = node(x)
            curr = curr.next_node
        
        if N.head:
            curr.next_node = N.head
        elif M.head:
            curr.next_node = M.head
            
        return result

def mergeList(self, N, M):
        """
        Merge 2 sorted Linked Lists

        Time Complexity: O(N+M)
        Space Complexity: O(1)
        """

        result = linkedList()
        if N.head.val <= M.head.val:
            result.head = node(N.popLeft())
        else:
            result.head = node(M.popLeft())
        
        curr = result.head

        while N.head and M.head:
            if N.head.val <= M.head.val:
                x = N.popLeft()
            else:
                x = M.popLeft()
            curr.next_node = node(x)
            curr = curr.next_node

        while N.head:
            x = N.popLeft()
            curr.next_node = node(x)
            curr = curr.next_node
        
        while M.head:
            x = M.popLeft()
            curr.next_node = node(x)
            curr = curr.next_node  
        return result

if __name__ == '__main__':
    import doctest
    doctest.testmod()
