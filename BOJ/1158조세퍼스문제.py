from collections import deque


def solution(N: int, K: int) -> list:
    """
    Args:
        N(int): 원형으로 앉아있는 사람 수. (1번부터 N번까지)
        K(int): 제거할 사람 번호, 첫 사람을 제거한 이후로는
                제거한 사람으로 부터 K번째에 앉아있는 사람을 제거한다.
        예를 들어 N=7, K=3일때,
        조세퍼스 순열은 <3, 6, 2, 7, 5, 1, 4>
    Returns:
        `list` of `int`: 조세퍼스 순열을 반환한다.
    """
    result: list = []
    left: list = []
    right = deque(range(1, N + 1))
    while left or right:
        for _ in range(K):
            if not right and left:
                right.extend(deque(left))  # 처음에 이부분 실수함
                left = []
            left.append(right.popleft())
        else:
            result.append(left.pop())
    return result


import unittest


class Test(unittest.TestCase):
    def test_oneN_biggerK(self):
        self.assertEqual([1], solution(1, 5))
        self.assertEqual([1], solution(1, 10))
        self.assertEqual([1], solution(1, 100))

    def test_twoN_biggerK(self):
        self.assertEqual([1, 2], solution(2, 1))
        self.assertEqual([2, 1], solution(2, 2))
        self.assertEqual([1, 2], solution(2, 3))

    def test_sevenN_smallerK(self):
        self.assertEqual([1, 2, 3, 4, 5, 6, 7], solution(7, 1))
        self.assertEqual([2, 4, 6, 1, 5, 3, 7], solution(7, 2))
        self.assertEqual([3, 6, 2, 7, 5, 1, 4], solution(7, 3))


if __name__ == "__main__":
    unittest.main()
    # import sys
    # N, K = [int(x) for x in sys.stdin.readline().split()]
    # result = ', '.join(str(x) for x in solution(N, K))
    # print('<{}>'.format(result))
