'''
counting Sort
1. Count the elements in the array. 배열A에 있는 각 원소들의 수를 세서 배열count에 저장.
2. Next, just iterate through the array of counters in increasing order.
   그 다음, 원소 수를 저장해 놓은 배열count의 각 원소를 오름 차순 순으로 순환하며 배열 A에 원소들을 저장한다.

Notice,
we have to know the range of the sorted values.
정렬하고자하는 배열이 가지고 있는 수의 범위를 알고 있어야한다.
'''

def countingSort(A,k):
    # A is consisted with integers range 0 to k
    n = len(A)
    # We need additional memory O(k)
    count = [0] * (k+1)
    for i in range(n):
        count[A[i]] += 1
    inx = 0
    for i in range(k+1):
        for j in range(count[i]): # smaller than O(n)
            print(A)
            A[inx] = i
            inx += 1
    return A


A = [4,2,1,3,5,2,1,2,3,5,0,0,0]
print(countingSort(A,len(set(A))))
