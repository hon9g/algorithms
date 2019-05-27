import unittest
class Test(unittest.TestCase):

	def test_size(self):
		self.assertEqual(0, len([]))
		self.assertEqual(1, len([1]))
		self.assertEqual(100, len([0]*100))

	def test_at(self):
		self.array = [1, 2, 3, 4, 5]
		self.assertEqual(1, self.array[0])
		self.assertEqual(2, self.array[1])
		self.assertEqual(5, self.array[-1])

	def test_push(self):
		self.array = [0]
		self.array.append(1)
		self.assertEqual(1, self.array[-1])

	def test_insert(self):
		self.array = [1, 2, 3]
		self.array.insert(0, 0)
		self.assertEqual([0, 1, 2, 3], self.array)
		self.array.insert(1, 9)
		self.assertEqual([0, 9, 1, 2, 3], self.array)

	def test_prepend(self):
		self.array = [1, 1, 1]
		self.array.insert(0, 9)
		self.assertEqual([9, 1, 1, 1], self.array)

	def test_pop(self):
		self.array = [4, 3, 2, 1, 0]
		self.assertEqual(0, self.array.pop())
		self.assertEqual(1, self.array.pop())
		self.assertEqual(2, self.array.pop())
		self.assertEqual(3, self.array.pop())
		self.assertEqual(4, self.array.pop())

	def test_remove(self):
		self.array = [0, 1, 2, 3, 4]
		self.array.remove(1)
		self.assertEqual([0, 2, 3, 4], self.array)
		self.array.remove(4)
		self.assertEqual([0, 2, 3], self.array)

	def test_delete(self):
		self.array = [0, 1, 2, 3, 4]
		del self.array[0]
		self.assertEqual([1, 2, 3, 4], self.array)
		del self.array[2:]
		self.assertEqual([1,2], self.array)
		del self.array[:]
		self.assertEqual([], self.array)

	def test_find(self):
		self.array = [10, 11, 12, 13, 10]
		self.assertEqual(0, self.array.index(10))
		self.assertEqual(4, self.array.index(10, 1))
		self.assertEqual(1, self.array.index(11))
		self.assertEqual(3, self.array.index(13))


if __name__ == '__main__':
	unittest.main()