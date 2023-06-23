from typing import List
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if r * c != len(mat[0]) * len(mat):
            return mat
        result = [[0] * c for i in range(r) ]
        r1, c1 = r-1, c-1
        for row in range(len(mat)-1, -1, -1):
            for col in range(len(mat[row])-1, -1, -1):
                # print(mat[row][col])
                result[r1][c1] = mat[row][col]
                r1 = r1 if c1 > 0 else r1 -1
                c1 = c1 -1 if c1 > 0 else c -1
        return result

print(Solution().matrixReshape([[1,2],[3,4]], 4, 1))
# print(Solution().matrixReshape([[1,2,3,4]], 2, 2))
 