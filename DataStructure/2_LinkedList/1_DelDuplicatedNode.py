"""
Build Linked List
"""
class Node():
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList():
	def __init__(self):
		self.head = None

def build_testcase(testcase: list):
	linked_list = LinkedList()
	for i in range(len(testcase)):
		if i == 0:
			linked_list.head = Node(testcase[0])
			node = linked_list.head
			continue
		node.next = Node(testcase[i])
		node = node.next
	return linked_list


"""
Solution
"""
def unique_only(linked_list):
	node = linked_list.head
	while node.next:
		next = node
		while next.next:
			next = next.next
			if node.data == next.data:
				node.next = next.next
		if not node.next:
			break
		node = node.next
	return linked_list


"""
Test
"""
import unittest
class Test(unittest.TestCase):
	def test_one_data(self):
		testcases = [[1],['a'],['apple']]

		for testcase in testcases:
			linked_list = build_testcase(testcase)
			real_answer = linked_list.head
			my_answer = unique_only(linked_list).head
			for i in range(len(testcase)):
				self.assertEqual(real_answer.data, my_answer.data)
				real_answer = real_answer.next
				my_answer = my_answer.next

	def test_unique_data(self):
		testcases = [[1, 2, 3], ['a', 'z', 'e'], ['apple', 'banana', 'monkey']]

		for testcase in testcases:
			linked_list = build_testcase(testcase)
			real_answer = linked_list.head
			my_answer = unique_only(linked_list).head
			for i in range(len(testcase)):
				self.assertEqual(real_answer.data, my_answer.data)
				real_answer = real_answer.next
				my_answer = my_answer.next

	def test_adjacent_duplicates(self):

		testcases = [[1, 1, 3], ['a', 'z', 'e', 'e'], ['apple', 'banana', 'banana', 'monkey']]
		real_answers = [[1, 3], ['a', 'z', 'e'], ['apple', 'banana', 'monkey']]

		for t in range(len(testcases)):
			real_answer = build_testcase(real_answers[t]).head
			my_answer =  unique_only(build_testcase(testcases[t])).head
			while real_answer.next:
				self.assertEqual(real_answer.data, my_answer.data)
				real_answer = real_answer.next
				my_answer = my_answer.next


if __name__ == "__main__":
	unittest.main()
