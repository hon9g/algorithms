'''
1. Arbitrarily, pick the pivot. (right most one in my code)
2. partitioning the array to sub-arrays.
3. recursionally, call quickSort function with sub-arrays.
'''

def quickSort1(nums: List[int]) -> List[int]:
    if len(nums) < 2: return nums
    pivot = nums[-1]
    lower = [ x for x in nums if x < pivot ]
    same = [ x for x in nums if x == pivot ]
    higher = [ x for x in nums if x > pivot ]
    return quickSort(lower)+ same + quickSort(higher)

A = [4,1,2]
print(quickSort(A))
