"""
백준 1110번, 더하기 사이클에 대한 솔루션.
"""


def solution(num: int) -> int:
    """
    Args:
        num(int): 0<=num<=99의 자연수
    Returns:
        int: 더하기 사이클에 따라 연산할 때,
             num이 자기 자신으로 돌아오게되는 연산 횟수.

        더하기사이클
            - 주어진 수가 10보다 작으면 앞에 0을 붙여 2자리로 만든후,
              각 자리의 숫자를 더한다. 이를 합이라 부른다.
            - 주어진 수의 가장 오른쪽 자리 수와 합을 더한다.
    """
    count: int = 0
    tail: int = num % 10
    head: int = (num - tail) // 10
    while 1:
        count += 1
        head, tail = tail, head
        tail = (head + tail) % 10
        if head * 10 + tail == num:
            break
    return count


def test():
    """
    >>> solution(26)
    4
    >>> solution(55)
    3
    >>> solution(1)
    60
    >>> solution(62)
    20
    """
    import doctest

    doctest.testmod()


if __name__ == "__main__":
    # N = int(input())
    # print(solution(N))
    test()
