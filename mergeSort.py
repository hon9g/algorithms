'''
Input: array of n numbers, unsorted.
Output: same numbers, sorted in increase order.

Pseuedo code

# merge step
C = output array [length n ]
A = 1st sorted array [length n//2]
B = 2nd sorted array [length n//2]
i = j = 1
for k=1 to n:
    if A(i) < B(j):
        C[k] = A(i)
        i ++
    else:
        C[k] = B(j)
        j ++
end
'''

