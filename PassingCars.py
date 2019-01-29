'''
array A = [ N integers ]
0 == travel to east
1 == travel to west

counting passing cars
pair of cars (P,Q)
0 <= P < Q < N,
when P travel to east Q travel to west
when P == 0 and Q == 1

e.g.
input: A = [0 ,1,0,1,1]
output: 5
becuase there are 5 fairs
(0,1) (0,3) (0,4) (2,3)
'''


'''
solution
1. find index that has a value 0. O(n)
2. make prefix sum. O(n)
3. if found index is k, add (total sum - total sum of index 0 to index k) to result.
4. go next found index, do #3 again.
total O(nm)

Trial 1: Task Score 70% Correctness 100% Performance 40%

WRONG at input 'random, length = ~100,000' 
 should return -1. 
I didn't read a part of instruction
### The function should return −1 if the number of pairs of passing cars exceeds 1,000,000,000. ###

Trial 2: Task Score 100% Correctness 100% Performance 100%
'''
def prefix_sum(A):
    n = len(A)
    P = [0] *(n+1)
    for i in range(1, n+1):
        P[i] = P[i-1] + A[i-1]
    return P

def count_pref(P,x,y):
    return P[y+1] - P[x]

def solution(A):
    # write your code in Python 3.6
    n = len(A)
    result = 0
    pref = prefix_sum(A)
    for i in range(n):
        if A[i] == 0:
            result += count_pref(pref, i, n-1)
            if result > 1000000000:
                return -1
    return result

''' 꼼꼼히 읽자 '''