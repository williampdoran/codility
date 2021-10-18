import sys


# class Solution:
#     def maxSubArray(self, nums) -> int:
#         max_sum = -sys.maxsize
#         for slice_size in range(1, len(nums)+1):
#             for j in range(0, len(nums)):
#                 if j + slice_size > len(nums):
#                     print("bang", j, j + slice_size)
#                     break
#                 slice = nums[j: j+slice_size]
#                 slice_sum = sum(slice)
#                 print(slice_size, j, slice, slice_sum)
#                 max_sum = max(slice_sum, max_sum)
#         return max_sum


2
3
4
5
6
7
8
9
class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxSubArray(self, A):
        print(A)
        max_so_far = max_ending_here = A[0]
        for index, item in enumerate(A[1:]):
            max_ending_here = max(item, max_ending_here + item)
            max_so_far = max(max_ending_here, max_so_far)
            print(A[1:index],max_ending_here, max_so_far, item)
        return max_so_far

print("Result", Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
# print("Result", Solution().maxSubArray([1]))
# print("Result", Solution().maxSubArray([5,4,-1,7,8]))
# print("Result", Solution().maxSubArray([-1]))
