def parenrhesis(S):
    """
    :param S(string): 길이 2 이상 50 이하 문자열. 괄호 기호로 이루어져 있다.
    :return:
        boolean: 괄호가 올바르게 구성되어있으면 True, 아니라면 False
    """
    left = 0
    for s in S:
        if '(' == s:
            left += 1
        elif ')' == s:
            if left == 0:
                return False
            left += -1
    return True if left == 0 else False

import unittest
class Test(unittest.TestCase):
    def test_True(self):
        self.assertEqual(True, parenrhesis('(()())((()))'))
        self.assertEqual(True, parenrhesis('()()()()(()()())()'))

    def test_False(self):
        self.assertEqual(False, parenrhesis('(())())'))
        self.assertEqual(False, parenrhesis('(((()())()'))
        self.assertEqual(False, parenrhesis('((()()(()))(((())))()'))
        self.assertEqual(False, parenrhesis('(()((())()('))

if __name__ == '__main__':
    # T = int(input())
    # for t in range(T):
    #     S = input()
    #     if parenrhesis(S):
    #         print('YES')
    #     else:
    #         print('NO')
    unittest.main()