def solution(M,N):
    """
    Args:
        M(int):
        N(int):
            M과 N은 10000이하의 자연수.
    Returns: None
        but print 2 line of int:
            line 1 -> M이상 N 이하 자연수 중 완전제곱수인 수들의 합
            line 2 -> 그 중 최솟값.

            만약 완전제곱수가 없다면 -1 출력.
    """

    n = 1
    min_square = N
    sum_square = 0
    while n*n <= N:
        if M <= n*n:
            if sum_square == 0:
                min_square = n * n
            sum_square += n*n
        n += 1
    if sum_square == 0:
        print(-1)
        return None
    print(sum_square)
    print(min_square)
    return None

from math import sqrt
def solution_sqrt(M,N):
    # math lib를 사용한다면
    a = int(sqrt(M))
    b = int(sqrt(N))

    min_square = 0
    sum_square = 0
    for n in range(a, b+1):
        if M <= n*n and n*n <= N:
            if sum_square == 0:
                min_square = n*n
            sum_square += n*n
    if sum_square == 0:
        print(-1)
        return None
    print(sum_square)
    print(min_square)
    return None

if __name__ == '__main__':
    M = int(input())
    N = int(input())
    solution_sqrt(M,N)

    solution(60, 100)
    solution(75, 80)
    solution_sqrt(60, 100)
    solution_sqrt(75, 80)