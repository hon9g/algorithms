'''
array A = { Non-empty, consisting N integers }

triplet = A[P] * A[Q] * A[R]
(0 <= P < Q < R < N)
(N is at least 3)

Goal: Find the maximal product of any triplet
'''


def solution(A):
    N = len(A)
    if N == 3:
        return A[0] * A[1] * A[2]
    A = sorted(A) # O(N * log(N))

    # All elements are positive
    # All elements are negative
    if A[0] >= 0 or A[N - 1] < 0:
        return A[N - 3] * A[N - 2] * A[N - 1]

    # Mixed, ( 4 <=N <=100000 )
    # -> 1 positive number --> A[0] * A[1] * A[N-1]
    if A[N - 2] < 0:
        return A[0] * A[1] * A[N - 1]
    # -> 2 positive number --> A[0] * A[1] * A[N-1]
    if A[N - 3] < 0:
        return A[0] * A[1] * A[N - 1]
    # -> more than 3 positive number --> compare A[0] * A[1] with A[N-3] * A[N-2]
    if A[0] * A[1] > A[N - 3] * A[N - 2]:
        return A[0] * A[1] * A[N - 1]
    return A[N - 3] * A[N - 2] * A[N - 1]
