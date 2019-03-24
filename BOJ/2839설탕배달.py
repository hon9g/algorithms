def solution(N):
    """
    Args:
        N(int): 봉지에 담아야하는 설탕 무게.
    Returns:
        int: 설탕을 담은 (3kg or 5kg)봉지의 최소 갯수 출력.
             봉지에 딱 떨어지게 담을 수 없다면 -1 출력.
    """
    fives = N//5
    n = N
    while True:
        n -= fives*5
        threes = n//3
        n -= threes*3
        if fives == 0 or n == 0:
            break
        fives += -1
        n = N
    if n == 0:
        print(threes+fives)
    else:
        print(-1)
    return None

def test():
    """
    아래 4가지 경우를 테스트 해볼 수 있는 케이스를 만든다.
        5kg 짜리 봉지만 사용하는 경우
        3kg 짜리 봉지만 사용하는 경우
        두 용량의 봉지를 모두 사용하는 경우
        어떤 경우에도 딱 맞아떨어지지 않는 경우

    >>> solution(18)
    4
    >>> solution(4)
    -1
    >>> solution(6)
    2
    >>> solution(9)
    3
    >>> solution(11)
    3
    >>> solution(25)
    5
    >>> solution(7)
    -1
    """
    import doctest
    doctest.testmod()
    solution(18)
    solution(4)
    solution(6)
    solution(9)
    solution(11)
    solution(25)
    solution(7)

if __name__ == '__main__':
    # N = int(input())
    # solution(N)

    test()