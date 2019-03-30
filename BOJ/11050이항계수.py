def binomial(n, k):
    """
    Args:
        n(int): 1 <= n <= 10
        k(int): 0 <= k <= n
    Returns:
        int: 이항계수 nCk 의 값
    """
    result = 1
    for i in range(k):
        result *= n
        n += -1
    for i in range(1, k+1):
        result = result // i
    return result

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