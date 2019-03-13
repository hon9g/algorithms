"""
**Note**
- Use prefix sum.
- It is just max slice sum problem, with special conditions.
"""

def solution(A):
    """
    :param A: A non-empty array A consisting of N integers.
            - Each element of array A is an integer within the range [−10,000..10,000].
            - N is an integer within the range [3..100,000]
    :return: An Integer, which is maximal sum of any double slice.

    The sum of double slice (X, Y, Z) is the total of
    A[X + 1] + A[X + 2] + ... + A[Y − 1] + A[Y + 1] + A[Y + 2] + ... + A[Z − 1].

    """
    pass