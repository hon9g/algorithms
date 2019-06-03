from typing import Tuple

def solution(M: int, N: int) -> Tuple[int, int]:
    """
    Args:
        M(int), N(int): M과 N은 10000이하의 자연수.
    Returns:
    	tuple(
        int: M이상 N 이하 자연수 중 완전제곱수인 수들의 합. 완전 제곱 수가 없다면 0. ,
        int: M이상 N 이하 자연수 중 완전제곱수인 수 중 최솟값. 완전 제곱 수가 없다면 0.
        )

        만약 완전제곱수가 없다면 line1: -1 출력.
    """
    n = 1
    min_square = 0
    sum_square = 0
    while n*n <= N:
        if M <= n*n:
            if sum_square == 0:
                min_square = n * n
            sum_square += n*n
        n += 1
    return sum_square, min_square


from math import sqrt

def solution_sqrt(M :int, N: int) -> Tuple[int, int]:
    """
    Args:
        M(int), N(int): M과 N은 10000이하의 자연수.
    Returns:
        tuple(
        int: M이상 N 이하 자연수 중 완전제곱수인 수들의 합. 완전 제곱 수가 없다면 0. ,
        int: M이상 N 이하 자연수 중 완전제곱수인 수 중 최솟값. 완전 제곱 수가 없다면 0.
        )
    """
    a = int(sqrt(M))
    b = int(sqrt(N))

    min_square = 0
    sum_square = 0
    for n in range(a, b+1):
        if M <= n*n and n*n <= N:
            if sum_square == 0:
                min_square = n*n
            sum_square += n*n
    return sum_square, min_square

def test():
    """
    >>> solution(60, 100)
    (245, 64)
    >>> solution(75, 80)
    (0, 0)
    >>> solution_sqrt(60, 100)
    (245, 64)
    >>> solution_sqrt(75, 80)
    (0, 0)
    """
    import doctest
    doctest.testmod()


if __name__ == '__main__':
    # M = int(input())
    # N = int(input())
    # sum_squares, min_of_squares = solution(M, N)
    # if sum_squares == 0:
    #     print(-1)
    # else:
    #     print(sum_squares)
    #     print(min_of_squares)
    test()