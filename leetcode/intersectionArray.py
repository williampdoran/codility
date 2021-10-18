class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counts1, counts2 = {}, {}
        result = list()
        for num in nums1:
            if num in counts1:
                counts1[num] += 1
            else:
                counts1[num] = 1
        for num in nums2:
            if num in counts2:
                counts2[num] += 1
            else:
                counts2[num] = 1
        for k in counts1.keys():
            if k in counts2:
                occurances = min(counts1[k], counts2[k])
                result = result + [k]*occurances
        return result