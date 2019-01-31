'''
array A = { 1. non-empty
            2. consisting N integers
            3. slice: (P,Q), when 0 <= P <= Q < N
                    , contains at least two elements.
            4. average of a slice: (A[P] + A[P+1] + ... + A[Q]) / (Q - P + 1)
            }

Goal: 가장 작은 평균을 갖은 slice의 맨 앞 원소의 index 찾기.
      Find the *starting position* of a slice whose average is minimal.
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
Goal: 가장 작은 부분집합을 포함한 slice 의 시작 원소의 인덱스를 반환하는 것.
조건: 부분집합의 크기는 2 이상이어야 한다.
결론 적으로 길이 2인 slice와 길이 3인 slice만 고려하면 된다.

길이 2인 slice를 고려해야하는 이유:
집합의 평균은  항상 가장 작은 원소보다 크다. 
집합{1,2}의 평균은 가장 작은 원소인 1 보다 큰 1.5이다.

[0, 4, 5, 7, 15]
집합 {4,1,2,8} 의 전체 평균은 3.75 이고, 
부분집합인 {4,1}의 평균은 2, {4,1,2}의 평균은 약 2.3 이다
{1,2}의 평균은 1.5, {1,2,8}의 평균은 약 3.6.
{2,8}의 평균은 5 이다.
가장 작은 평균을 갖은 부분집합은 최소한의 원소를 가지고 있다. 
# {1,2}의 평균은 1.5이 가장 작으므로, return 1

가장 작은 원소가 집합의 평균보다 항상 크기가 작듯이,
가장 작은 부분집합의 평균은 모집합의 평균보다 항상 크기가 작다.


순서를 {8,4,2,1}로 바꿔도, 총 평균은 3.75. 
{8,4}의 평균은 6,  {8,4,2}의 평균은 약 4.6.
{4,2}의 평균은 3, {4,2,1}의 평균은 약 2.3.
{2,1}의 평균은 1.5로 가장 작은 평균을 갖은 부분집합은 최소한의 원소를 갖고 있다.
# {2,1}이 가장 작으므로, return 2

순서를 {1,8,2,4}로 바꿔도, 총 평균은 3.75.
{1,8}의 평균은 4.5, {1,8,2}의 평균은 약 3.6.
{8,2}의 평균은 5, {8,2,4}의 평균은 약 4.6.
{2,4}의 평균은 3으로 가장 작은 평균을 갖은 부분집합은 최소한의 원소를 갖고 있다.
# {2,4}가 가장 작으므로, return 2

따라서, 가장 작은 원소를 갖고있는 부분집합의 평균만 구하면된다.
(부분집합의 원소 갯수는 2개 이상이어야 한다는 조건을 만족시키는)
짝수의 원소를 갖고 있는 slice 가장 작은 slice의 길이는 2

길이 3의 slice를 고려해야하는 이유:
홀수의 원소를 갖고 있는 가장 작은 slice 길이는 3이 라고들 많이 하는데,
홀수 갯수 array 에서도 range 2씩 한칸씩 옆으로 가면서 확인하니까, 최소 단위는 2임.
길이 3을 고려해야하는 다른 이유가 있는 것 같음

'''

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

    for x in range(N - 2):
        tmp_score = avg(P, x, 3)
        if score > tmp_score:
            score = tmp_score
            index = x

    return index


'''
짝수개의 집합에서는 길이 3의 slice를 고려하지 않게 코드를 짰을때,
아래와 같은 문제가 있음.

Task Score 90%  Correctness 80%  Performance 100%
[10, 10, -1, 2, 4, -1, 2, -1] the solution returned a wrong answer (got 2 expected 5).

{-1,2,-1}의 평균은 0임.

이 경우에 대한 증명 확인하기.
'''
