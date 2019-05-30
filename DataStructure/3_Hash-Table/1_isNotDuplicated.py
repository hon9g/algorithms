"""
중복은 없는가

문자열이 주어졌을 때, 이 문자열에 같은 문자가 중복되어 등장하지 않는지 확인하는 알고리즘을 작성하라.
"""

def unique_chracters(S :str):
	"""
	Args:
		S(str): 알파벳 소문자.
	Returns:
		문자열 내에 중복되는 문자가 없을 때 True.  있다면 False.
	"""
	if 26 < len(S):
		return False
	is_duplicated = [False] * 26
	for s in S:
		key = ord(s) - ord('a')
		if is_duplicated[key]:
			return False
		is_duplicated[key] = True
	return True

"""
자료구조를 추가로 사용하지 않고 풀 수 있는 알고리즘 또한 고민하라.
"""

def inplace_solution(S: str):
	"""
	Args:
		S(str): 알파벳 소문자.
	Returns:
		문자열 내에 중복되는 문자가 없을 때 True.  있다면 False.
	"""
	if len(S) == 1:
		return True
	S = sorted(S)
	for i in range(1,len(S)):
		if S[i-1] == S[i]:
			return False
	return True

"""
Test
"""
import unittest
class Test(unittest.TestCase):
	def test_false_with_hash(self):
		self.assertEqual(False, unique_chracters('aaa'))
		self.assertEqual(False, unique_chracters('aab'))
		self.assertEqual(False, unique_chracters('azz'))
		self.assertEqual(False, unique_chracters('asdfghjkla'))

	def test_true_with_hash(self):
		self.assertEqual(True, unique_chracters('a'))
		self.assertEqual(True, unique_chracters('abc'))
		self.assertEqual(True, unique_chracters('zxcv'))

	def test_false_inplace(self):
		self.assertEqual(False, inplace_solution('aaa'))
		self.assertEqual(False, inplace_solution('aab'))
		self.assertEqual(False, inplace_solution('azz'))
		self.assertEqual(False, inplace_solution('asdfghjkla'))

	def test_true_inplace(self):
		self.assertEqual(True, inplace_solution('a'))
		self.assertEqual(True, inplace_solution('abc'))
		self.assertEqual(True, inplace_solution('zxcv'))

if __name__ == '__main__':
	Test()