from math import sqrt
def solution(nums):
    """
    Args:
        nums(`list` of `int`): 각 원소는 1000 이하 자연수.
    :return:
        int: 주어진 숫자 중 소수의 갯수.
    """
    nums = sorted(nums)
    count, n = 0, int(sqrt(nums[-1]))+1
    is_prime = [False, False] + [True]*(nums[-1]-1)

    while 1 < n:
        for n2 in range(2, (nums[-1]//n)+1):
            is_prime[n * n2] = False
        n += -1
    # print(is_prime)
    for num in nums:
        if is_prime[num]:
            count += 1
    print(count)

def test():
    """
    >>> solution([1, 3, 5, 7])
    3
    >>> solution([2, 4, 6, 8])
    1
    >>> solution([1])
    0
    >>> solution([111])
    0
    >>> solution([13])
    1

    """
    import doctest
    doctest.testmod()
    cases = [[1, 3, 5, 7], [2, 4, 6, 8],[1],[111],[13]]
    for case in cases:
        solution(case)

if __name__ ==  '__main__':
    # N = int(input())
    # nums = [int(x) for x in input().split()]
    # solution(nums)
    test()
