def great_common_divisor(a,b):
    if a < b:
        a, b = b, a
    a = a % b
    if a == 0:
        return b
    return great_common_divisor(a, b)

def solution(a,b):
    """
    Args:
        a(int): 10,000이하의 자연수
        b(int): 10,000이하의 자연수
    Returns:
        print gcd(int): 최대공약수를 출력한다.
        print lcm(int): 최소공배수를 출력한다.
    """
    gcd = great_common_divisor(a, b)
    print(gcd)
    lcm = a*b//gcd
    print(lcm)


def test():
    '''
    >>> great_common_divisor(6, 15)
    3
    >>> great_common_divisor(1024, 6)
    2
    >>> solution(24, 18)
    6
    72
    >>> solution(6, 15)
    3
    30
    >>> solution(1024, 6)
    2
    3072
    '''
    import doctest
    doctest.testmod()

if __name__ == '__main__':
    # a, b = [int(x) for x in input().split()]
    # solution(a,b)
    test()