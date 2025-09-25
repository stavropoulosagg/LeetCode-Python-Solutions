# You are given row x col grid representing a map where grid[i][j] = 1 
# represents land and grid[i][j] = 0 represents water. 
# 
#  Grid cells are connected horizontally/vertically (not diagonally). The grid 
# is completely surrounded by water, and there is exactly one island (i.e., one or 
# more connected land cells). 
# 
#  The island doesn't have "lakes", meaning the water inside isn't connected to 
# the water around the island. One cell is a square with side length 1. The grid 
# is rectangular, width and height don't exceed 100. Determine the perimeter of 
# the island. 
# 
#  
#  Example 1: 
#  
#  
# Input: grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
# Output: 16
# Explanation: The perimeter is the 16 yellow stripes in the image above.
#  
# 
#  Example 2: 
# 
#  
# Input: grid = [[1]]
# Output: 4
#  
# 
#  Example 3: 
# 
#  
# Input: grid = [[1,0]]
# Output: 4
#  
# 
#  
#  Constraints: 
# 
#  
#  row == grid.length 
#  col == grid[i].length 
#  1 <= row, col <= 100 
#  grid[i][j] is 0 or 1. 
#  There is exactly one island in grid. 
#  
# 
#  Related Topics Array Depth-First Search Breadth-First Search Matrix 👍 7158 ?
# ? 413


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        perimeter = 0

        def dfs(start_r, start_c):
            nonlocal perimeter
            stack = [(start_r, start_c)]
            visited.add((start_r, start_c))

            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            while stack:
                r, c = stack.pop()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                        perimeter += 1
                    elif grid[nr][nc] == 0:
                        perimeter += 1
                    elif (nr, nc) not in visited:
                        visited.add((nr, nc))
                        stack.append((nr, nc))

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    dfs(i, j)
                    return perimeter  # only one island
        return 0
# leetcode submit region end(Prohibit modification and deletion)
