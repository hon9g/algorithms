'''
Nucleotides(char) in the sequence, has impact factor (int)
{ 'A':1 , 'C':2 , 'G':3 , 'T':4 }
S = { consisting N Nucleotides(char) }

There are M number of queries.
P, Q = { consisting M integers, represent index of range in S }
'''

'''
solution 2; prefix_count:
1. prefix_count: 각 알파벳 별로 count 수를 누적해서 저장 
2. check: m 번 iterate 하면서 각 알파벳 별 누적 count를 알파벳[Q+1] - 알파벳[P]를 해보면,
    해당 range 안의 알파벳 occurrence 를 알 수 있다. 존재하지 않으면 0, 존재하면 0 이상의 숫자를 return 받는다.
   (작은 impact factor 를 갖은 알파벳 부터 체크)

Time Complexity: O(N + M)
Task Score 100%   Correctness 100%   Performance 100%
'''
def prefix_count(S):
    N = len(S)
    A = [0]*(N+1)
    C = [0]*(N+1)
    G = [0]*(N+1)
    for n in range(1, N+1):
        A[n] = A[n-1]
        C[n] = C[n-1]
        G[n] = G[n-1]
        if S[n-1] == 'A':
            A[n] += 1
        elif S[n-1] == 'C':
            C[n] += 1
        elif S[n-1] == 'G':
            G[n] += 1
    return A, C, G

def check(T,x,y):
    return T[y+1]-T[x]

def solution(S, P, Q):
    A, C, G = prefix_count(S) # O(N)
    result = []
    M = len(P)
    for m in range(M):
        # O(1) * O(M)
        if check(A, P[m], Q[m]) > 0:
            result += [1]
        elif check(C, P[m], Q[m]) > 0:
            result += [2]
        elif check(G, P[m], Q[m]) > 0:
            result += [3]
        else:
            result += [4]
    return result

'''
solution 1: 
1. countS: 각 알파벳에 해당하는 S[index]를 네 개의 알파벳 별로 저장.
2. 특정 range 속 가장 작은 값을 찾아낼 떄 impact factor 시퀀스에서 iterate 하는게 아니라, 
    알파벳 별로 저장해놓은 인덱스에서 P[m] 과 Q[m] 비교연산한다.

Time Complexity: O(N * M)   
Task Score 75%   Correctness 100%   Performance 33%

Problem: almost_all_same_letters 과 large_random 에서 Time Out.
         시퀀스 전체에서 한 알파벳이 차지하는 비율이 높다면. 알파벳 별로 나누어 저장한 의미가 없어짐.
         impact factor가 큰 G나 T를 찾을 때에도, 오히려 그냥 해당 range를 비교 연산하는 것보다 느릴 수 밖에 없다.
'''

def countS(S):
    ind = {'A':[],'C':[],'G':[],'T':[]}
    for s in range(len(S)):
        ind[S[s]] += [s]
    return ind.values()


def min(A, C, G,x,y):
    for a in range(len(A)):
        if A[a] >= x and A[a] <= y:
            return [1]
    for c in range(len(C)):
        if C[c] >= x and C[c] <= y:
            return [2]
    for g in range(len(G)):
        if G[g] >= x and G[g] <= y:
            return [3]
    return [4]


def solution(S, P, Q):
    M = len(Q)
    result = []
    A, C, G, _ = countS(S)
    for m in range(M):
        result += min(A, C, G, P[m], Q[m])
    return result