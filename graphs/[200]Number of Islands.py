# Given an m x n 2D binary grid grid which represents a map of '1's (land) and 
# '0's (water), return the number of islands. 
# 
#  An island is surrounded by water and is formed by connecting adjacent lands 
# horizontally or vertically. You may assume all four edges of the grid are all 
# surrounded by water. 
# 
#  
#  Example 1: 
# 
#  
# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1
#  
# 
#  Example 2: 
# 
#  
# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Output: 3
#  
# 
#  
#  Constraints: 
# 
#  
#  m == grid.length 
#  n == grid[i].length 
#  1 <= m, n <= 300 
#  grid[i][j] is '0' or '1'. 
#  
# 
#  Related Topics Array Depth-First Search Breadth-First Search Union Find 
# Matrix 👍 24285 👎 586


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = (len(grid), len(grid[0]))
        visited = set()
        islands = 0

        def dfs(r,c):
            if (r,c) in visited:
                return
            visited.add((r,c))

            directions = [(0,1),(1,0),(-1,0),(0,-1)]
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                if not (0 <= nr < rows and 0 <= nc < cols):
                    continue
                if grid[nr][nc] == "1":
                    dfs(nr,nc)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j]=="1" and (i,j) not in visited:
                    islands += 1
                    dfs(i,j)

        return islands


# leetcode submit region end(Prohibit modification and deletion)
