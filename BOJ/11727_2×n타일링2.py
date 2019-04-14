def solution(N):
    """
    Args:
        N(int): 주어진 직사각형의 넓이. 1 ≤ N ≤ 1,000
    Returns: 2×n 크기의 직사각형을 채우는 방법의 수를 10,007로 나눈 나머지를 출력한다.
    """
    nums_of_cases = [0, 1, 3]
    if N < 3:
        return nums_of_cases[N]
    for _ in range(3, N+1):
        nums_of_cases[1], nums_of_cases[2] = nums_of_cases[2], (nums_of_cases[1]*2) + nums_of_cases[2]
    return nums_of_cases[2]% 10007


if __name__ == '__main__':
    N = int(input())
    print(solution(N))