def solution(N):
    """
    Args:
        N(int): 11보다 작은 양수
    Returns:
        int: N을 1, 2 ,3 의의 합으로 나타내는 방법의 수
    """
    cases = [ None, 1, 2, 4, 7]
    if N < 5:
        return cases[N]
    for n in range(5, N+1):
        cases.append(cases[n-3]+cases[n-2]+cases[n-1])
    return cases.pop()


if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        N = int(input())
        print(solution(N))
