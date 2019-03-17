"""Note
[Task description & result of this solution](https://app.codility.com/demo/results/trainingVFHZJW-Y9B/)
I wrote an algorithm that works well with input values ​​that contain positive numbers, and
I modified it slightly to work well when input values ​​consisting of only negative numbers come in.
"""

def solution(A):
    """  Detected time complexity: O(N)   Task Score 100%  Correctness 100%  Performance 100%
    Find a maximum sum of a compact subsequence of array elements.
    :param A:  A is an array consisting of N integers.
            - Each element of array A is an integer within the range [−1,000,000..1,000,000]
            - N is an integer within the range [1..1,000,000]
    :return: Maximum sum of any slice of A.
            - An integer within the range [−2,147,483,648..2,147,483,647]
            - A pair of integers (P, Q), such that 0 ≤ P ≤ Q < N, is called a slice of array A.
    """
    max_ending, max_slice = 0, A[0]
    for i in range(len(A)):
        max_ending += A[i]
        max_ending = max(A[i], max_ending)
        max_slice = max(max_ending, max_slice)
    return max_slice

"""
Example test:   [3, 2, -6, 4, 0]
OK

Your test case: [-500]
Returned value: -500

Your test case: [-10, -500]
Returned value: -10

Your test case: [-500, -10]
Returned value: -10
"""


def solution(A):
    """ Detected time complexity: O(N)   Task Score 100%  Correctness 100%  Performance 100%
    Find a maximum sum of a compact subsequence of array elements.
    :param A:  A is an array consisting of N integers.
            - Each element of array A is an integer within the range [−1,000,000..1,000,000]
            - N is an integer within the range [1..1,000,000]
    :return: Maximum sum of any slice of A.
            - An integer within the range [−2,147,483,648..2,147,483,647]
            - A pair of integers (P, Q), such that 0 ≤ P ≤ Q < N, is called a slice of array A.
    """
    max_ending = 0
    max_slice = A[0]
    for a in A:
       max_ending += a
       if  max_slice < max_ending:
           max_slice = max_ending
       if max_ending < 0:
           max_ending = 0
       # print(max_ending, max_slice)
    return max_slice


def solution(A):
    """Detected time complexity: O(N) or O(N**3)   Task Score 84%  Correctness 100%  Performance 60%

    :param A:  A is an array consisting of N integers.
            - Each element of array A is an integer within the range [−1,000,000..1,000,000]
            - N is an integer within the range [1..1,000,000]
    :return: Maximum sum of any slice of A.
            - An integer within the range [−2,147,483,648..2,147,483,647]
            - A pair of integers (P, Q), such that 0 ≤ P ≤ Q < N, is called a slice of array A.
    """
    n = len(A)
    result = 2147483648*-1  # Don't need to initialize the value in this way.
                            # In the first iteration, I will turns to value A[0].
    for p in range(n):
        sum = 0
        for q in range(p,n):
            sum += A[q]
            if result < sum:
                result = sum
    return result