def solution(N):
    """
    Args:
        N(int): 자연수.
    Return: N이상 2*N이하 구간에 존재하는 소수의 갯수.
    """
    is_prime = [True]*(2*N +1)
    is_prime[0] = is_prime[1] = False
    # print(is_prime)
    n = 2
    while n*n <= 2*N:
        composite = n*(N//n)
        while composite <= 2*N:
            is_prime[composite] = False
            composite += n
        n += 1
    count = 0
    for i in range(N+1,2*N+1):
        if is_prime[i]:
            count += 1
    print(count)

def test():
    """
    >>> solution(1)
    1
    >>> solution(10)
    4
    >>> solution(13)
    3
    >>> solution(100)
    21
    >>> solution(1000)
    135
    >>> solution(10000)
    1033
    >>> solution(100000)
    8392
    """
    import doctest
    doctest.testmod()
    cases = [1, 10, 13, 100, 1000, 10000, 100000]
    for case in cases:
        solution(case)

if __name__=='__main__':
    while 1:
        N = int(input())
        if N == 0:
            break
        solution(N)

    test()