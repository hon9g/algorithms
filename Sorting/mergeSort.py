'''
Merge Sort 병합정렬: Divide the unsorted array into two halves, sort each half separately and then just merge them.
                     정렬하고자 하는 배열을 반으로 쪼개서, 각각 정렬한 후 합친다.
# Divide Step: halved each part until it become individual element.
               개별 원소만 남을 때까지 부분집합들을 계속 반으로 쪼갠다.
# Merge Step: Just repeatedly choose the lower of the first elements of the two merged parts.
              두개로 쪼개진 부분집합을 하나로 합칠때는, 반복적으로 첫번째 원소끼리만 비교해서 작은 것을 먼저 가져오면 된다.

'''
'''
Divide step
middle = len(S)//2
return 
'''

def mergeSort(S):
    n = len(S)
    if n < 2:
        return S

    C = [0] * n
    A, B = mergeSort(S[n//2:]), mergeSort(S[:n//2])
    i, j = 0, 0

    for k in range(n):
        # A, B 둘중 하나의 정렬이 끝났으면,
        # 남은 다른 한 쪽의 배열을 C[:k] 자리에 붙여주고 끝낸다.
        if i == len(A):
            C = C[:k] + B[j:]
            return C
        elif j == len(B):
            C = C[:k] + A[i:]
            return C

        # 각자 배열에서 아직 정렬되지 않은 맨 앞자리의 원소끼리 비교연산
        if A[i] < B[j]:
            C[k] = A[i]
            i+=1
        else:
            C[k] = B[j]
            j+=1

    return C

print(mergeSort([5,2,3,1,0,10,50]))