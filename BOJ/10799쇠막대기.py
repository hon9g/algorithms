def num_of_piece(stick):
    """
    Args:
        S(str): 최대길이 100,000의 괄호 기호로 이루어진 문자열
    Returns:
        int: 레이저로 잘린 쇠막대기 조각 수
    """
    left, piece = 0, 0
    if stick[0] == '(':
        left += 1
    for i in range(1, len(stick)):
        if stick[i] == ')':
            if stick[i-1] == '(':
                left += -1
                piece += left
            else:
                piece += 1
                left += -1
        elif stick[i] == '(':
            left += 1
    return piece

import unittest
class Test(unittest.TestCase):
    def test_small(self):
        self.assertEqual(0, num_of_piece('()'))
        self.assertEqual(2, num_of_piece('(())'))
        self.assertEqual(4, num_of_piece('((()))'))
        self.assertEqual(3, num_of_piece('(()())'))
    def test_medium(self):
        self.assertEqual(17,num_of_piece('()(((()())(())()))(())'))
        self.assertEqual(24, num_of_piece('(((()(()()))(())()))(()())'))

if __name__ == '__main__':
    # s = input()
    # print(num_of_piece(s))
    unittest.main()