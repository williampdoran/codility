from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        start = 0
        r = len(matrix)
        c = len(matrix[0])
        end = r * c -1
        while start <= end:
            mid = (start + end)//2
            mid_value = matrix[mid//c][mid%c]
            if mid_value > target:
                end = mid +1
            elif mid_value < target:
                start = mid -1
            else:
                return True
        return False
print(Solution().searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))