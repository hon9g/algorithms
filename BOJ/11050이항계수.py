def binomial(n, k):
    """
    Args:
        n(int): 1 <= n <= 10
        k(int): 0 <= k <= n
    Returns:
        int: 이항계수 nCk 의 값
    """
    if n == k or k == 0:
        return 1
    molecule = 1
    for i in range(1, n+1):
        molecule *= i
    denominator = 1
    for i in range(1,k+1):
        denominator *= i
    for i in range(1,n-k+1):
        denominator *= i
    return molecule//denominator

import unittest
class test(unittest.TestCase):
    def test_binomial(self):
        self.assertEqual(10, binomial(5, 2)) #expected, actual
        self.assertEqual(1, binomial(5, 5))
        self.assertEqual(1, binomial(5, 0))
        self.assertEqual(120, binomial(10, 3))

if __name__ == '__main__':
    # n, k = [int(x) for x in input().split()]
    # print(binomial(n,k))
    unittest.main()