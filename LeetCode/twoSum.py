"""
solution for twoSum
https://leetcode.com/problems/two-sum/
"""

"O(N)"
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        passed = {}
        for idx, val in enumerate(nums):
            n_needed = target - val
            if n_needed in passed:
                return [passed[n_needed], idx]
            passed[val] = idx
        return []


"O(N**2)"
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        answer, i = [], 0
        while answer == [] and i+1 < len(nums):
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j] == target:
                    answer = [i,j]
                    break
            i += 1
        return answer