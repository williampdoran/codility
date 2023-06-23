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


    def binSearch(self, nums, target):
        print(nums)
        if len(nums) == 0:
            return -1
        elif len(nums) == 1:
            return nums[0] if nums[0] == target else -1
        else:
            start = 0
            end = len(nums) -1
            mid = (start + end) // 2
            if nums[mid] == target:
                return nums[mid]
            elif nums[mid] > target:
                return self.binSearch(nums[:mid], target)
            else:
                return self.binSearch(nums[mid +1:end+1], target)

nums = [-1,0,3,5,9,12]
target = 9

#print(Solution().search(nums, target))
print(Solution().binSearch(nums, target))
#print(Solution().search([5], 5))