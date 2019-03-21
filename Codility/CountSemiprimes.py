def is_prime(N):
    """
    Args:
        N(int): Maximum number that should care.
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

    while prime**2 <= N+1:
        if prime_flags[prime]:
            num_prime_dividers[prime*prime] += 2
            prime2 = N//prime
            while prime2 > prime:
                if prime_flags[prime2]:
                    num_prime_dividers[prime2*prime] += 2
                prime2 += -1
        prime += 1

    pref_answers = [0] * (N + 1)
    for i in range(4, N+1):
        pref_answers[i] = pref_answers[i - 1]
        if num_prime_dividers[i] == 2:
            pref_answers[i] += 1

    answers = []
    for k in range(len(P)):
        answer = pref_answers[Q[k]] - pref_answers[P[k]-1]
        answers += [answer]
    return answers


'''
"""Note
[Test result](https://app.codility.com/demo/results/training882UTH-H3B/)
[Test result](https://app.codility.com/demo/results/trainingQAAK3X-898/)
I got 66/100 points in two attempts,
with 100 point of Correctness  and 40 points in Performance.
Detected TimeComplexity was so complex:
O(N * log(log(N)) + M * N) or O(M * N ** (3/2))
In the second attempt, I tried to do the logic used in the first try a little more precisely.
Here are where were changed in the second attempt.

    prime = 2
        while prime**2 <= N+1:
            if prime_flags[prime]:
                num_prime_dividers[prime*prime] += 2
                prime2 = N//prime
                while prime2 > prime:
                    if prime_flags[prime2]:
                        num_prime_dividers[prime2*prime] += 2
                    prime2 += -1
            prime += 1

[Test result](https://app.codility.com/demo/results/trainingTNQ9GE-T3H/)
In the third attempt, got Task Score 100%  Correctness 100%  
Detected Performance was O(N * log(log(N)) + M)

I did not really change main logic. 

Looking at the time complexities detected in previous attempts, 
I found that the issue was inside of k times repetition of P and Q array to make the final answer.

# This part
    for k in range(len(P)):
        cnt_semiprime = 0
        for i in range(P[k],Q[k]+1):
            if num_prime_dividers[i] == 2:

I was using the prefix sum to fix the code so that it will end in k times when I get the final answer.

    pref_answers = [0] * (N + 1)
    for i in range(4, N+1):
        pref_answers[i] = pref_answers[i - 1]
        if num_prime_dividers[i] == 2:
            pref_answers[i] += 1
            
    answers = []
    for k in range(len(P)):
        answer = pref_answers[Q[k]] - pref_answers[P[k]-1]
        answers += [answer]
    return answers
'''
