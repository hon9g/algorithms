def gcd(a: int, b: int):
    if a < b:
        a, b = b, a
    a %= b
    if a == 0:
        return b
    return gcd(a, b)

def solution(N: int,nums: list):
    """
    Args:
        N(int): 리스트 nums의 길이. ( 1 < N ≤ 100 )
        nums(`list` of `int`):  각 원소의 값은 1000000을 넘지 않는다.
    Returns:
        nums에 존재하는양의 정수들의 가능한 모든 쌍의 GCD의 합.
    """
    if N == 1:
        return 0
    sum_gcds, x  = 0, 0
    while x < N-1:
        for y in range(x+1, N):
            sum_gcds += gcd(nums[x], nums[y])
        x += 1
    print(sum_gcds)

def test():
    """
    >>> solution(4, [10, 20, 30, 40])
    70
    >>> solution(3, [7, 5, 12])
    3
    >>> solution(3, [125, 15, 25])
    35
    """
    import doctest
    doctest.testmod()

if __name__ == '__main__':
    # T = int(input())
    # for t in range(T):
    #     nums = [int(x) for x in input().split()]
    #     solution(nums[0], nums[1:])
    test()
