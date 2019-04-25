def solution(N: int, P: list):
    costs = [P[0]]
    for i in range(1, N):
        costs.append(P[i])
        for j in range(i):
            costs[i] = max(costs[i], costs[j]+P[i-j-1])
    return costs[-1]%1000000000

def false_solution(N: int, P: list):
    values = []
    for idx, cost in enumerate(P):
        values.append([idx, cost/(idx+1)])
    values.sort(key= lambda element : element[1], reverse=True)
    cost = 0
    idx = 0
    while 0 < N:
        num_card = values[idx][0]+1
        if num_card <= N:
            cost += P[num_card-1]
            N -= num_card
        else:
            idx += 1
            if idx == len(values):
                break
    return cost%1000000000

def test():
    """
    >>> solution(4, [1, 5, 6, 7])
    10
    >>> solution(5, [10, 9, 8, 7, 6])
    50
    >>> solution(10, [1, 1, 2, 3, 5, 8, 13, 21, 34, 55])
    55
    >>> solution(10, [5, 10, 11, 12, 13, 30, 35, 40, 45, 47])
    50
    >>> solution(4, [5, 2, 8, 10])
    20
    >>> solution(4, [3, 5, 15, 16])
    18
    """
    import doctest
    doctest.testmod()

if __name__ == '__main__':
    N = int(input())
    P = [int(x) for x in input().split()]
    print(solution(N, P))
    # test()