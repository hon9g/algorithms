def solution(N):
    """
    Args:
        N(int): 1 ≤ N ≤ 1,000
    Returns:
        int: 2xN 크기의 직사각형을 1x2 또는 2x1 타일로 채우는 방법의 수을 10,007로 나눈 나머지
    """
    if N < 4:
        return N
    grandmother, mother = 2, 3
    for _ in range(4, N+1):
        grandmother, mother = mother, grandmother+mother
    return mother % 10007


import unittest
class Test(unittest.TestCase):

    def test_case(self):
        self.assertEqual(1, solution(1))
        self.assertEqual(2, solution(2))
        self.assertEqual(3, solution(3))
        self.assertEqual(5, solution(4))
        self.assertEqual(8, solution(5))
        self.assertEqual(13, solution(6))

if __name__ == '__main__':
    # N = int(input())
    # print(solution(N))
    unittest.main()
    """
    1.
    테스트케이스를 직접 손으로 그려서 확인해보던 중,
    2x6 사이즈의 경우의 수를 셀 때, 하나를 빼먹었고
    잘못된 테케를 가지고 방정식을 만드는 실수를 했다.
    2.
     마지막 % 10007 같은 작은 조건을 까먹지말자.
    """