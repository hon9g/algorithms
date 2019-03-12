"""
[Task description & result of this solution](https://app.codility.com/demo/results/trainingJRZPP6-545/)

Task Score 100%
Correctness 100%
Performance 100%

**Note**
- Use stack for finding leader.
- Use prefix sum to count the number of leaders in a sub-sequence and make it easier to compare.
"""

def solution(A):
    """
    :param A: A non-empty array A consisting of N integers is given
    :return: number of equi leaders.
    """
    n = len(A)
    if n == 1:
        return 0

    stack = ["Bottom", A[0]]
    for i in range(1, n):
        if stack[-1] == A[i] or stack[-1] == "Bottom":
            stack += [A[i]]
        else:
            stack.pop()

    prefix_occur = []
    occur = 0
    for i in range(n):
        if A[i] == stack[-1]:
            occur += 1
        prefix_occur += [occur]

    equi_leader = 0
    for i in range(n - 1):
        if prefix_occur[i] / (i + 1) > 0.5 and (prefix_occur[-1] - prefix_occur[i]) / (n - i - 1) > 0.5:
            equi_leader += 1

    return equi_leader