def gcd(a: int, b: int) -> int:
    if a < b:
        a, b = b, a
    a = a % b
    if a == 0:
        return b
    return gcd(a, b)

def solution(A: int, B: int) -> int:
    """
    Args:
        A(int), B(int): 각각 1 ≤ A, B ≤ 45,000 사이의 양수.
    Returns:
        int: A와 B의 최소공배수.
    """
    return A*B//gcd(A, B)

def test():
    """
    >>> solution(1, 45000)
    45000
    >>> solution(6, 10)
    30
    >>> solution(13, 17)
    221
    """
    import doctest
    doctest.testmod()

if __name__ == '__main__':
    # T = int(input())
    # for t in range(T):
    #     A, B = [int(x) for x in input().split()]
    #     print(solution(A, B))
    test()
