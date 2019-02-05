'''
INPUT:  3 integer.
    A, B =  within the range [0 ~ 2,000,000,000];
            A <= B.
    K = within the range [1 ~ 2,000,000,000]
OUTPUT: The number of integers within the range [A..B] that are divisible by K

when (A <= i <= B),
    if i % K = 0:
        count += 1
return count
'''

'''
O(1) solution: (B//K) - ((A-1)//K)
'''

def solution(A, B, K):
    result = B//K
    if A != 0:
        result -= (A-1)//K
    else:
        # Notice, "0%K == 0", The value 0 is divisible by K for all K that are allowed.
        # Because, in this quiz, the definition of divisible means there is no remainder after dividing.
        result += 1
    return result

'''
O((B-A)/K) slower solution: Task Score 62%  Correctness 100%  Performance 25%

when (A <= K < B),
Count Multiple of K within range (A to B)

Do not need to consider, smaller numbers than K.
(A <= K < B) --> consider range K to B
(A <= B = K) --> just return 1
(A <= B < K) --> just return 0
'''

def solution(A, B, K):
    if B < K:
        return 0

    count = 0
    i = A//K

    if A == i*K: # it include case "0%K == 0"
        count += 1
    while 1:
        i+= 1
        if i*K > B:
            break
        count += 1
    return count
