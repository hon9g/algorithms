"""Note
[Task description & result of this solution](https://app.codility.com/demo/results/training882UTH-H3B/)

I need to retry for better performance soon.
"""
def is_prime(N):
    """
    Args:
        N(int):
    Returns:
        list of bool: If prime then True, If not then False.
    """
    prime_flags = [True for x in range(N + 1)]
    prime_flags[0] = prime_flags[1] = False
    n = 2
    while n * n <= N:
        multiple = n * n
        while multiple <= N:
            prime_flags[multiple] = False
            multiple += n
        n += 1
    return prime_flags

def solution(N, P, Q):
    """
    A semiprime is a natural number that is the product of two prime numbers. (not necessarily distinct)
    The first few semiprimes are 4, 6, 9, 10, 14, 15, 21, 22, 25, 26.

    Args:
        N(int): within the range [1..50,000]
        P(`list` of `int`), Q(`list` of `int`):

            These arrays represent the K th querie's range of target set as from P[K] to Q[k]

            1 ≤ P[K] ≤ Q[K] ≤ N
            Each element of arrays P, Q is an integer within the range [1..N]
            The length of the list is within the range [1..30,000]

    Returns:
        list of int: list which is contain the consecutive answers to all the queries.
                     answer is the number of semiprimes within the range (P[K], Q[K]).
        semiprimes of queries in order.

    """
    prime_flags = is_prime(N)
    num_prime_dividers = [0] * (N + 1)
    prime = 2
    while prime**2 <= N:
        if prime_flags[prime]:
            one_more_prime = prime
            while one_more_prime*2 <= N:
                if prime * one_more_prime > N:
                    break
                if prime_flags[one_more_prime]:
                    num_prime_dividers[prime*one_more_prime] += 2
                one_more_prime += 1
        prime += 1
    print(num_prime_dividers, prime, one_more_prime)
    answers = []
    for k in range(len(P)):
        cnt_semiprime = 0
        for i in range(P[k],Q[k]+1):
            if num_prime_dividers[i] == 2:
                cnt_semiprime += 1
        answers += [cnt_semiprime]
    return answers

print(solution(10, [1], [10]))