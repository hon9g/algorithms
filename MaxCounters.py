'''
Input: N counters initially set to 0, non-empty array A of M integers
Output: final counter

function
A[K] = X
1. 1 <= X <= N, increase 1 for  index X
2. X = N+1, set all counter to the max value of counter
'''


def solution(N, A):
    # write your code in Python 3.6
    # Task Score 88% Correctness 100% Performance 80%
    # O(N + M)
    print(N, len(A))
    counter = [0] * N
    max = 0
    for i in range(len(A)):
        print(i - 1, counter)
        print(i)
        if A[i] == N + 1:
            print("reset")
            counter = [max] * N

        else:
            print("increase")
            counter[A[i] - 1] += 1
            if counter[A[i] - 1] > max:
                max = counter[A[i] - 1]
    return counter