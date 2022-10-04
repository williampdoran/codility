from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, n1 in enumerate(nums):
            for j, n2 in enumerate(nums):
                if i !=j and n1 + n2 == target:
                    return [i,j]
# traverse the list, and make of map of index to value, traverse the list again looking for target - elem in the map.
    def twoSum2(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        idx = {nums[i]:i for i in range(len(nums))}
        for i in range(len(nums)):
            need = target - nums[i]
            if need in idx and idx[need] != i:
                return [i, idx[need]]

nums = [2,7,11,15]
target = 9

# print(Solution().twoSum(nums, target))
print(Solution().twoSum2(nums, target))