def solution(A, B, C, D):
    """
    Args:
        A(str), B(str), C(str), D(str): 자연수로 구성되어있는 문자.  (1 ≤ A, B, C, D ≤ 1,000,000)
    Returns:
        int: A와 B를 붙인 수와 C와 D를 붙인 수의 합.
             두 수 A와 B를 붙이는 것은 A의 뒤에 B를 붙이는 것을 의미한다
    """
    return int(A+B) + int(C+D)


def test():
    """
    >>> solution('10', '20', '30', '40')
    4060
    """
    import doctest
    doctest.testmod()


if __name__ == '__main__':
    A, B, C, D = [x for x in input().split()]
    print(solution(A, B, C, D))
    # test()