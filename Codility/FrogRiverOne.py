'''
Flog want to get the other side of river
0, start position
X+1, opposite bank

A = consistion N interger
A[K] = the position where one leaf falls at time K

Goal: find the earliest time when the frog can jump to the other side of the river.

The frog can cross only when leaves appear at every position across the river from 1 to X
(that is, we want to find the earliest moment when all the positions from 1 to X are covered by leaves)

        N and X are integers within the range [1..100,000]; O(N) or O( n *log(n))
        each element of array A is an integer within the range [1..X].
'''


'''
Task Score 100%  Correctness 100%  Performance 100%
Time Complexity: O(n)
'''
def solution(X, A):
    # write your code in Python 3.6
    leaves = [0]*(X+1)
    count = 0
    for i in range(len(A)):
        if leaves[A[i]] == 0:
            leaves[A[i]] = 1
            count += 1
            if count == X:
                return i
    return -1


assert solution(5, [1,3,1,4,2,3,5,4]) == 6