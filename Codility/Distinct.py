'''
array A = { consisting N integers }
return number of distinct values in array A.
'''

def solution(A):
    # Detected time complexity: O(N*log(N)) or O(N)
    # Task Score 100%  Correctness 100%  Performance 100%
    return len(set(A))