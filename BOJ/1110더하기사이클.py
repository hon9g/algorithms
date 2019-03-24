def solution(N):
    """
    Args:
        N(int): 0<=N<=99의 자연수
    Returns:
        int: 더하기 사이클에 따라 연산할 때,
             N이 자기 자신으로 돌아오게되는 연산 횟수.

        더하기사이클
            - 주어진 수가 10보다 작으면 앞에 0을 붙여 2자리로 만든후,
              각 자리의 숫자를 더한다. 이를 합이라 부른다.
            - 주어진 수의 가장 오른쪽 자리 수와 합을 더한다.
    """
    count = 0
    tail = N%10
    head = (N - tail)//10
    while 1:
        count += 1
        head, tail = tail, head
        tail = (head+tail)%10
        if head*10 + tail == N:
            break
    print(count)

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
    test_inputs = [26, 55, 1]
    for input in test_inputs:
        solution(input)

if __name__ == '__main__':
    test()

    # N = int(input())
    # solution(N)