'''
Score 100 %
O(n) or O(n log n)
'''

def solution(A):
    # write your code in Python 3.6
    if len(A) == 0:
        return 1
    A = sorted(A)
    if A[-1] != len(A)+1:
        return len(A)+1
    for i in range(len(A)):
        if i+1 != A[i]:
            return i+1