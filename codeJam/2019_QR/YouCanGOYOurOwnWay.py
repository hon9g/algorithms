def solution(N, P):
    """
    Args:
        N(int): Size of the maze (it is square). 2 ≤ N ≤ 50000.
        P(str): This is Lydia's path, consisted by char 'S' and 'E'.
    Returns:
        result(str): Valid path through the N by N maze that does not conflict with Lydia's path.
    """
    result = ''
    for p in P:
        if 'S' == p:
            result += 'E'
        else:
            result += 'S'
    return result



if __name__ == '__main__':
    T = int(input())
    for t in range(T):
        N = int(input())
        P = input()
        print('Case #{}: {}'.format(t+1, solution(N, P)))