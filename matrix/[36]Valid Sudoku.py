# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be 
# validated according to the following rules: 
# 
#  
#  Each row must contain the digits 1-9 without repetition. 
#  Each column must contain the digits 1-9 without repetition. 
#  Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 
# without repetition. 
#  
# 
#  Note: 
# 
#  
#  A Sudoku board (partially filled) could be valid but is not necessarily 
# solvable. 
#  Only the filled cells need to be validated according to the mentioned rules. 
# 
#  
# 
#  
#  Example 1: 
#  
#  
# Input: board = 
# [["5","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: true
#  
# 
#  Example 2: 
# 
#  
# Input: board = 
# [["8","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: false
# Explanation: Same as Example 1, except with the 5 in the top left corner 
# being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is 
# invalid.
#  
# 
#  
#  Constraints: 
# 
#  
#  board.length == 9 
#  board[i].length == 9 
#  board[i][j] is a digit 1-9 or '.'. 
#  
# 
#  Related Topics Array Hash Table Matrix 👍 12078 👎 1238


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            myrow = [x for x in row if x!="."]
            if len(myrow) != len(set(myrow)):
                return False

        for col in list(zip(*board)):
            mycol = [x for x in col if x!="."]
            if len(mycol) != len(set(mycol)):
                return False

        for box_row in range(0,9,3):
            for box_col in range(0,9,3):
                square = [board[r][c]
                          for r in range(box_row, box_row+3)
                          for c in range(box_col, box_col+3)
                          if board[r][c]!="."]

                if len(square) != len(set(square)):
                    return False

        return True


# leetcode submit region end(Prohibit modification and deletion)
