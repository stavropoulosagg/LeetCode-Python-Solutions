# You are given an m x n binary matrix grid. An island is a group of 1's (
# representing land) connected 4-directionally (horizontal or vertical.) You may assume 
# all four edges of the grid are surrounded by water. 
# 
#  The area of an island is the number of cells with a value 1 in the island. 
# 
#  Return the maximum area of an island in grid. If there is no island, return 0
# . 
# 
#  
#  Example 1: 
#  
#  
# Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,
# 0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,
# 0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]
# ]
# Output: 6
# Explanation: The answer is not 11, because the island must be connected 4-
# directionally.
#  
# 
#  Example 2: 
# 
#  
# Input: grid = [[0,0,0,0,0,0,0,0]]
# Output: 0
#  
# 
#  
#  Constraints: 
# 
#  
#  m == grid.length 
#  n == grid[i].length 
#  1 <= m, n <= 50 
#  grid[i][j] is either 0 or 1. 
#  
# 
#  Related Topics Array Depth-First Search Breadth-First Search Union Find 
# Matrix 👍 10442 👎 215


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        rows, cols = (len(grid), len(grid[0]))
        visited = set()
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        maximum = 0

        def dfs(r,c):
            if (r,c) in visited:
                return 0
            visited.add((r,c))
            res = 1
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    res += dfs(nr,nc)
            return res

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    maximum = max(maximum,dfs(i,j))

        return maximum
# leetcode submit region end(Prohibit modification and deletion)
