'''
array A = { 1. non-empty
            2. consisting N integers, (2<=N)
            3. slice: range(A[P],A[Q]), when 0 <= P <= Q < N
                    , contains at least two elements.
            4. average of a slice: (A[P] + A[P+1] + ... + A[Q]) / (Q - P + 1)
            }

Goal: Find the *starting position* of a slice whose average is minimal.
      Performance should be O(n).
'''

'''
brute force solution:: O(N ** 2)
'''

def prefix_sum(A):
    N = len(A)
    P = [0]*(N+1)
    for n in range(1, N+1):
        P[n] = P[n-1]+A[n-1]
    return P

def avg(P,x,y):
    return (P[y+1]-P[x])/(y-x+1)

def bruteForceSolution(A):
    N = len(A)
    P = prefix_sum(A)
    score = 10001
    index = 0
    for x in range(N):
        for y in range(1, N-x):
            tmp_score = avg(P, x, x+y)
            if tmp_score < score:
                score = tmp_score
                index = x
    return index

'''
Time Complexity: O(n)
Task Score 100%  Correctness 100%  Performance 100%
'''

def prefix_sum(A):
    N = len(A)
    P = [0]*(N+1)
    for n in range(1, N+1):
        P[n] = P[n-1]+A[n-1]
    return P


def avg(P, x, n):
    print(x, x + n, (P[x + n] - P[x]) / (n))
    return (P[x + n] - P[x]) / (n)


def solution(A):
    N = len(A)
    P = prefix_sum(A)
    print(P)
    score = 10001
    index = 0

    for x in range(N - 1):
        print(x)
        tmp_score = avg(P, x, 2)
        if score > tmp_score:
            score = tmp_score
            index = x
    if N == 2:
        return index

    for x in range(N - 2):
        tmp_score = avg(P, x, 3)
        if score > tmp_score:
            score = tmp_score
            index = x

    return index

'''
Goal: 가장 작은 부분집합을 포함한 slice 의 시작 원소의 인덱스를 반환하는 것.
조건: 부분집합의 크기는 2 이상이어야 한다.

결론 적으로 길이 2인 slice와 길이 3인 slice만 고려하면 된다.

집합의 평균은  항상 가장 작은 원소보다 크다. 
집합{1,2}의 평균은 가장 작은 원소인 1 보다 큰 1.5이다.
가장 작은 원소가 집합의 평균보다 항상 크기가 작듯이,
가장 작은 부분집합의 평균은 모집합의 평균보다 항상 크기가 작다.

Every slice must be of size 2 or 3. Slices of bigger sizes are created from such smaller slices. 
Therefore should any bigger slice have an optimal value, all sub-slices must be the same, for this case to hold true. 
Should this not be true, one of the sub-slices must be the optimal slice. 
The others being bigger. 
Therefore we check all possible slices of size 2/3 and return the smallest one. 
가장 작은 길이의 부분집합은 2와 3이다.
짝수의 원소를 갖은 집합은 길이 2의 부분집합으로 충분하지만, 
홀수 길이의 부분집합을 커버하기 위해 길이 3의 부분집합을 필요로 하다고들한다.


(-1+1+(-1)+1)/4 = 0
(-1+1)/2, (1+(-1))/2, (-1+1)/2 = 0
(-1+1+(-1))/3 = 약 -0.3
(1+(-1)+1)/3 = 약 0.6

(1 + (-1) + 1 + (-1)) / 4 = 0
(1+(-1))/2, (-1+1)/2, (1+(-1))/2 = 0
(1+(-1)+1)/3 = 약 0.6
(-1+1+(-1))/3 = 약 -0.3


array 총 길이가 3일때

길이 2인 slice가 최소 평균:
(1+0+1)/3 = 약 0.6
(1,0)/2, (0,1)/2 = 0.5 

(0+(-1)+0)/3 = 약 -0.3
(0+(-1))/2, (-1+0)/2 = -0.5

길이 3의 slice가 최소평균:
(0+1+0)/3 = 약 0.3
(0,1)/2, (1,0)/2 = 0.5

(-1+1+(-1))/3  = 약 -0.3
(-1+1)/2, (1+(-1))/2 = 0 

'''

