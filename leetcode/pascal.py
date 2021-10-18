from typing import List
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1]] * numRows
        if numRows == 1:
            return [[1]]
        for row in range(1, numRows):
            result[row] = [1]* (row +1)
            for col in range(1, row):
                result[row][col] = result[row -1][col] + result[row -1][col -1]
        return result

print(Solution().generate(5))