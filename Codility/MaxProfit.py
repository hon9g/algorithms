"""
[Task description & result of this solution](https://app.codility.com/demo/results/trainingF8NZFN-NFV/)

Task Score 100%
Correctness 100%
Performance 100%

"""

def solution(A):
    """
    :param A: An array A consisting of N integers is given.
        - Each element of array A is an integer within the range [0..200,000].
          Daily prices of a stock share for a period of N consecutive days;
        - N: An integer within the range [0..400,000];

    :return: An Integer which is maximum possible profit from one transaction.
              If it was impossible to gain any profit return 0.
        If a single share was bought on day P and sold on day Q, where 0 ≤ P ≤ Q < N
        - transaction is equal to A[Q] - A[P], provided that A[Q] ≥ A[P].
        - Otherwise, the transaction brings loss of A[P] - A[Q].
    """
    if A == []:
        return 0
    max_slice = 0
    bought = 400000
    for i in range(len(A)):
        if bought > A[i]:
            # print("change bought day at", i)
            bought = A[i]
        else:
            max_slice = max(max_slice, A[i]-bought)
        # print( bought, max_slice)
    return max_slice