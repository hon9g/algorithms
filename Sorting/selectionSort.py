'''
Slection sort 선택정렬
1.  Find the minimal element in array.
    Swap it with the first element of an array.
    배열에서 가장 작은 수를 찾은 후, 맨 앞의 원소와 자리를 바꿔준다.
2.  Next, sort the rest of the array, without the first element, in the same way.
    그 다음, 정렬된 맨 앞원소를 제외한 배열의 나머지를 정렬한다.
3. Iterate it n times. 2번 반복.
'''

def findSmallest(A):
    smallest_inx = 0
    smallest = A[smallest_inx]
    for i in range(1, len(A)): # O(n)
        if smallest > A[i]:
            smallest_inx = i
            smallest = A[smallest_inx]
    return smallest_inx


def selectionSort(A):
    # takes O(n^2)
    # there is 'findSmallest, O(n)' inside of O(n) times iteration.
    for i in range(len(A)):
        print(A)
        smallest_inx = findSmallest(A[i:]) + i
        A[i], A[smallest_inx] = A[smallest_inx],  A[i]
    return A


A = [5,1,3,5,2,0]
# print(findSmallest(A))
print(selectionSort(A))
