class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        j = 0
        for i in range(0, m+n):
            if j >= n:
                break
            if nums2[j] <= nums1[i]:
                right_slice = nums1[i:-1]
                nums1[i] = nums2[j]
                nums1[i+1:] = right_slice
                j += 1
        if j < n:
            nums1[m+j:] = nums2[j:]
        print(nums1)

# print(Solution().merge([4,0,0,0,0,0], 1, [1,2,3,5,6], 5))
Solution().merge([1,2,3,0,0,0], 3, [2,5,6], 3)