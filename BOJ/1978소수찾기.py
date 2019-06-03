def solution(nums: list) -> int:
    """
    Args:
        nums(`list` of `int`): 각 원소는 1000 이하 자연수.
    Returns:
        int: 주어진 숫자 중 소수의 갯수.
    """
    nums = sorted(nums)
    count: int = 0
    n: int = 2
    is_prime = [False, False] + [True] * (nums[-1] - 1)
    while n * n <= nums[-1]:
        composite = n * n
        while composite <= nums[-1]:
            is_prime[composite] = False
            composite += n
        n += 1
    for num in nums:
        if is_prime[num]:
            count += 1
    return count


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


if __name__ == "__main__":
    # N = int(input())
    # nums = [int(x) for x in input().split()]
    # print(solution(nums))
    test()
