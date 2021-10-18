

class Solution:
    def containsDuplicate(self, nums) -> bool:
        counts = {}
        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1
        return any(count > 1 for count in counts.values())

l1 = [3,3]
print(Solution().containsDuplicate(l1))