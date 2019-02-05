'''
INPUT:  array A = consisting N integers
        (0 <= N <= 100,000. Expected time complexity `O(N)` or `O( n *log(n))`)

Goal: Find triangular

def triangular(A):
    when ( 0 <= P < Q < R ),
        if
            |  A[P] + A[Q] > A[R]  &  A[Q] + A[R] > A[P]  &  A[R] + A[P] > A[Q]  |    than it is triangular.
            return 1
        else:
            return 0


'''

'''
Task Score 100%  Correctness 100%  Performance 100%

Idea: 
1.  It is only necessary to check whether the case with the combinations of smallest deviation satisfies the condition.
    가장 작은 편차를 갖은 조합이 조건을 충족시키는지 여부만 확인하면된다.
2. In an ordered array, combinations with consecutive elements have smallest deviation among all possible combinations.
    정렬된 배열에서 연속 원소끼리의 조합이 가능한 모든 조합 중에서 가장 작은 편차를 갖는다.

P Q R 은 서로 다른 양의 정수이다.
부등호 오른쪽 인덱스 정해줄 때는 P Q R 끼리의 순서의 의미 있다.하지만 가능한 케이스 3가지 경우 다 만족해야하기 때문에 결과적으로 순서의 의미 없다.
따라서 주어진 배열 그대로의 순서를 고집할 필요 없이, 배열을 정렬한 후 사용해도 괜찮다.

'''


def solution(A):
    N = len(A)
    if N < 3:
        return 0
    A = sorted(A)
    for P in range(N-2):
        Q, R = P+1, P+2
        if A[P] < A[Q] + A[R] and A[Q] < A[P] + A[R] and A[R] < A[Q] + A[P]:
            return 1
    return 0



'''
on my first attempt 
I thought start middle of sorted array can make faster answer.

What I need to consider
- In an sorted array, The three consecutive elements have less variation than the other combinations.
- Therefore, It's okay to only consider three consecutive elements in sorted array.
- However, It is meaningless to start searching near the median of the entire array.
- I should consider all 3 consecutive combination in sorted array.
'''
def solution(A):
    N = len(A)
    if  N < 3:
        return 0
    A = sorted(A)
    Q = N//2
    while 1:
        P, R = Q - 1, Q + 1
        if A[P] < A[Q]+A[R] and A[Q] < A[P]+A[R] and A[R] < A[Q]+A[P]:
            return 1
        if P > 0 and R < N-1:
            left = abs(A[P] - A[P-1])
            right = abs(A[R+1] - A[R])
            if left > right:
                Q += 1
            else:
                Q -= 1
        else:
            break
    return 0