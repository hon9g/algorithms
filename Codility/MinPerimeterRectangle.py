"""Note
[Task description & result of this solution](https://app.codility.com/demo/results/training648G6G-JXY/)
"""

def solution(N):
    """ 100 points  Detected time complexity:O(sqrt(N))
    :param N: The area of some rectangle as a Integer within the range [1..1,000,000,000].
    :return: Minimal perimeter of any rectangle as a Integer.
    """
    perimeter = N + 1
    for i in range(1,N):
        if i*i >= N:
            if i*i == N:
                perimeter = i + (N // i)
            break
        if N%i == 0:
            perimeter = i + (N // i)
    return perimeter * 2