"""Note
[Task description & result of this solution](https://app.codility.com/demo/results/trainingPRJUAN-RTV/)

If N is 24, the solution should return 8.
Because 24 has 8 factors (1, 2, 3, 4, 6, 8, 12, 24).

And You can find the pattern,
1 * 24 = 24   --> There are 2 factors.
2 * 12 = 24   --> There are 2 factors.
3 * 8 = 24    --> There are 2 factors.
4 * 6 = 24    --> There are 2 factors.

So, you don't need to check the factor, after Square root of N.
However, if the Square root of N is the natural number, you should count it.
I wil give an example. If N is 4, solution should return 3.
Because 4 has 3 factors (1, 2, 4). And 2 is the square root of 4.

1 * 4 = 4   --> There are 2 factors.
2 * 2 = 4   --> There are 1 factor.
"""
def solution(N):
    """100 points  Detected time complexity:O(sqrt(N))

    :param N: A positive Integer within the range [1..2,147,483,647].
    :return: The number of N's factors.
    """
    factors = 0
    for i in range(1, N):
        if i*i >= N:
            if i*i == N:
                factors += 1
            break
        if N % i == 0:
            factors += 2
    return factors