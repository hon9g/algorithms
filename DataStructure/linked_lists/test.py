from doubly_linked_list_from_scratch import DoublyLinkedList


def test():
    """
	>>> ll = DoublyLinkedList()
	>>> len(ll)
	0
	>>> ll.append('one')
	>>> len(ll)
	1
	>>> print(ll)
	one->NULL
	>>> ll.appendleft("zero")
	>>> len(ll)
	2
	>>> print(ll)
	zero->one->NULL
	>>> ll.insert(-1, "two")
	>>> len(ll)
	3
	>>> print(ll)
	zero->one->two->NULL
	>>> ll.insert(0, "added at left-side")
	>>> print(ll)
	added at left-side->zero->one->two->NULL
	>>> ll.popleft()
	'added at left-side'
	>>> print(ll)
	zero->one->two->NULL
	>>> ll.pop()
	'two'
	>>> ll.reverse()
	>>> print(ll)
	one->zero->NULL
	>>> ll.rotate(-1)
	>>> print(ll)
	zero->one->NULL
	>>> ll.rotate(1)
	>>> print(ll)
	one->zero->NULL
	>>> ll.rotate(len(ll))
	>>> print(ll)
	one->zero->NULL
	>>> ll.rotate(3)
	>>> print(ll)
	zero->one->NULL
	>>> ll.insert(2, "two")
	>>> print(ll)
	zero->one->two->NULL
	>>> ll.insert(0, "head")
	>>> print(ll)
	head->zero->one->two->NULL
	>>> len(ll)
	4
	>>> ll.count("head")
	1
	>>> ll.popleft()
	'head'
	>>> ll.count("head")
	0
	>>> ll.remove("one")
	>>> print(ll)
	zero->two->NULL
	>>> ll.clear()
	>>> len(ll)
	0
	"""
    import doctest

    doctest.testmod()


if __name__ == "__main__":
    test()
