def solution(N):
    """
    Args
        N(int): 정수. 0 < N <= 10**6.
    Returns:
        int: N을 1로 만들기위해 필요한 연산의 횟수.

        연산은 3 종류가 있다.
        1. if X%3 == 0: X //= 3
        2. if X%2 == 0: X //= 2
        3. X += -1

    """

    counters = [0, 0, 1, 1]
    if N < 4:
        return counters[N]

    for i in range(4, N + 1):
        counters.append(counters[i-1]+1)
        if i % 2 == 0:
            counters[i] = min(counters[i//2]+1, counters[i])
        if i % 3 == 0:
            counters[i] = min(counters[i//3]+1, counters[i])
    return counters[N]


def false_solution(N):
    """
    2 로도 나누어지고 3으로도 나누어지는 경우를 고려하지 못함.

    Args
        N(int): 정수. 0 < N <= 10**6.
    Returns:
        int: N을 1로 만들기위해 필요한 연산의 횟수.

        연산은 3 종류가 있다.
        1. if X%3 == 0: X //= 3
        2. if X%2 == 0: X //= 2
        3. X += -1

    """

    counters = [0, 0, 1, 1]
    if N < 4:
        return counters[N]

    for i in range(4, N+1):
        if i % 2 == 0:
            counters.append(1 + min(counters[i//2], counters[i-1]))
        elif i % 3 == 0:
            counters.append(1 + min(counters[i//3], counters[i-1]))
        else:
            counters.append(1 + counters[i-1])
    return counters[N]

import unittest
class Test(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(solution(1),0)

    def test_one(self):
        self.assertEqual(solution(2), 1)
        self.assertEqual(solution(3), 1)

    def test_two(self):
        # 4-1=3 + 3을 1로 만드는 최소 횟수는 1 => 2회
        self.assertEqual(solution(4), 2)
        # 6//3 = 3, 3을 1로 만드는 최소 횟수는 1 => 2회
        self.assertEqual(solution(6), 2)
        # 9//3 = 3, 3을 1로 만드는 최소횟수는 1 => 2회
        self.assertEqual(solution(9), 2)

    def test_three(self):
        # 5-1=4, 4을 1로 만드는 최소횟수는 2 => 3회
        self.assertEqual(solution(5), 3)
        # 7-1=6, 6을 1로 만드는 최소횟수는 2 => 3회
        self.assertEqual(solution(7), 3)
        # 10-1=9, 9를 1로 만드는 최소횟수는 2 => 3회
        self.assertEqual(solution(10), 3)
        self.assertEqual(solution(12), 3)

    def test_four(self):
        self.assertEqual(solution(11), 4)


if __name__ == '__main__':
    N = int(input())
    print(solution(N))
    # unittest.main()