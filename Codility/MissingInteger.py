'''
input: array A of N integers.
output: smallest positive integer (greater than 0)
'''


def solution(A):
    # write your code in Python 3.6
    # Task Score 100% Correctness100% Performance 100%
    # O(N) or O(N * log(N))
    answer = 1
    array = sorted(A)
    for i in range(len(A)):
        if array[i] > 0 and array[i] == answer:
            answer += 1
    return answer