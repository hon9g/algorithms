'''
1. Arbitrarily, pick the pivot.
2. partitioning the array to sub-arrays (smaller and bigger part).
3. recursionally, call quickSort function with sub-arrays.
'''

def quickSort(A):
    # Base step
    if len(A) < 2:
        return A

    # Recursion step
    pivot = A[0]
    ## partitioning to sub-arrays
    smaller = []
    bigger = []
    for i in range(1, len(A)):
        if A[i] < pivot:
            smaller += [A[i]]
        else:
            bigger += [A[i]]
    return quickSort(smaller) + [pivot] + quickSort(bigger)


        
A = [4,1,2]
print(quickSort(A))