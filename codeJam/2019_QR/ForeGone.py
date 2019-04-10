def Constructive_solution(N):
    """ It pass all Test set
    Args:
        N(int): A positive integer, which contain number 4. 1 < N < 10**100.
    Returns:
         A(int), B(int): A + B = N, A and B could not contain number 4.
    """
    A = B = ''
    ten = 0
    for n in str(N):
        if n == '4':
            A += '3'
            B += '1'
        else:
            A += n
            B += '0'
    return int(A), int(B)

def BruteForce_solution(N):
    """ It only pass  Test set 1 (1 < N < 10**5).
    Args:
        N(int): A positive integer, which contain number 4. 1 < N < 10**100.
    Returns:
         A(int), B(int): A + B = N, A and B could not contain number 4.
    """
    A, B = 0, N
    while True:
        A += 3
        B += -3
        if '4' in str(B):
            continue
        elif '4' in str(A):
            continue
        else:
            break
    return A, B



if __name__ == '__main__':
    T = int(input())
    for t in range(T):
        N = int(input())
        A, B = [x for x in Constructive_solution(N)]
        print('Case #{}: {} {}'.format(t+1, A, B))