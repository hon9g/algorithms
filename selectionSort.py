
def findSmallest(A):
    smallest_inx = 0
    smallest = A[smallest_inx]
    for i in range(1, len(A)):
        if smallest > A[i]:
            smallest_inx = i
            smallest = A[smallest_inx]
    return smallest_inx


def selectionSort(A):
    # takes O(n^2)
    # iterate 'findSmallest == O(n)' O(n) times
    sorted_A = []
    for i in range(len(A)):
        smallest_inx = findSmallest(A)
        sorted_A += [A.pop(smallest_inx)]
        # A.remove(smallest)
    return sorted_A


A = [5,1,3,5,2,0]
print(findSmallest(A))
print(selectionSort(A))
