class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def searchRec(nums, target, start, end):
            if start == end:
                if nums[start] == target:
                    return start
                else:
                    return -1
            mid = (start + end) // 2
            elem = nums[mid]
            if elem < target:
                return searchRec(nums, target, mid + 1, end)
            elif elem > target:
                return searchRec(nums, target, start, mid)
            else:
                return mid

        start = 0
        end = len(nums) - 1
        return searchRec(nums, target, start, end)

nums = [-1,0,3,5,9,12]
target = 9

print(Solution().search(nums, target))
print(Solution().search([5], 5))