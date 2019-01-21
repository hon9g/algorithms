
'''
INPUT: A = sorted array, i = value want to fine
OUTPUT: If value i is in A, return the index of it,
        if not return -1.
'''

def binarySearch(A,i):
    low = 0
    high = len(A) -1
    while low <= high:
        mid = (low + high) // 2
        if A[mid] == i:
            return mid
        elif A[mid] < i:
            low = mid+1
        else:
            high = mid
    return -1



A = [0,1,2,3,4,5,6]
i = 1000

print(binarySearch(A,i))
print ()