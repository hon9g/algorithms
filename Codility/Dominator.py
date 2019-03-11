'''
Detected time complexity: O(N*log(N)) or O(N)
Task Score 100%
Correctness 100%
Performance 100%

### Note
    At first occur error with input which is `extreme_empty_and_single_item `
    I shound check all conditions such as
        - N is an integer within the range [0..100,000];
        - each element of array A is an integer within the range [−2,147,483,648..2,147,483,647].

    My code without `For empty_and_single_item cases` part only consider cases which contains more than 2 items.
'''

def solution(A):

    ### For empty_and_single_item cases ###
    if A == []:
        return -1
    n = len(A)
    if n == 1:
        return 0
    #######################################

    stack = ["Bottom", A[0]]
    for i in range(1, n):
        if stack[-1] == A[i] or stack[-1] == "Bottom":
            stack += [A[i]]
        else:
            stack.pop()
    count = 0
    for i in range(n):
        if stack[-1] == A[i]:
            count += 1
            inx = i
    dominator = -1
    if count > n//2:
        dominator = inx
    return dominator