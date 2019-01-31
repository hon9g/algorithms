'''
array A: consisting of N integers(positive,0,negative) is given
         non-empty
         represent number of on a tape

any integer P: 0 < P < N

return: absolute difference between the sum of first part and sum of second part
        that can be
'''

def slow_solution(A):
    '''
    score 53. correctness 100%, performance 0%.
    It takes O(N^2).
    because
    I have for loop range n/2
    inside of for loop: sum() takes O(n)

    I need to find solution with out sum() inside of for loop.
    '''
    best = abs(sum(A[:1]) - sum(A[1:]))

    for i in range(1, (len(A) // 2) + 1):

        left = abs(sum(A[:i]) - sum(A[i:]))
        right = abs(sum(A[-i:]) - sum(A[:-i]))
        if best > left:
            best = left
        if best > right:
            best = right
    return best

def solution(A):
    '''Task Score100% Correctness100% Performance100%'''
    total = sum(A)
    minimum = 9999999999999 # I wanna find more smarter way.
    first = 0
    for i in range(len(A)-1):
        first += A[i]
        temp = abs(total - (first*2))
        if minimum > temp:
            minimum = temp
    return minimum

'''To-do: Task case 다양하게 고려해보기
          Python 내장 함수 Time complexity 알아두기'''