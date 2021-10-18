from typing import List
class Solution:
    def col(self, slice, matrix):
        return [row[slice] for row in matrix]

    def counts(self, numbers):
        counts = [0] * 10
        for num in numbers:
            if num != ".":
              counts[int(num)] += 1
        return counts

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        valid = True
        for i in range(0,9):
            row_i = board[i]
            col_i = [row[i][0] for row in board]
            square_top_left = (i//3) * 3
            square_bottom_right = (i % 3) * 3

            t = [r[square_bottom_right: square_bottom_right+3] for r in board[square_top_left:square_top_left + 3]]
            square_i = [item for sublist in t for item in sublist]
            # print(row_i)
            # print(col_i)
            # print(square_top_left,square_bottom_right)
            # print(square_i)
            # print("-------------------")
            valid = valid and all(x <= 1 for x in self.counts(row_i)) and all(x <= 1 for x in self.counts(col_i)) and all(x <= 1 for x in self.counts(square_i))
        return valid

board = [["5","3",".",".","7",".",".",".","."]
    ,["6",".",".","1","9","5",".",".","."]
    ,[".","9","8",".",".",".",".","6","."]
    ,["8",".",".",".","6",".",".",".","3"]
    ,["4",".",".","8",".","3",".",".","1"]
    ,["7",".",".",".","2",".",".",".","6"]
    ,[".","6",".",".",".",".","2","8","."]
    ,[".",".",".","4","1","9",".",".","5"]
    ,[".",".",".",".","8",".",".","7","9"]]
print(Solution().isValidSudoku(board))