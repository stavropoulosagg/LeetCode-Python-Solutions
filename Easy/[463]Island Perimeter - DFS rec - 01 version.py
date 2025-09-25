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
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        perimeter = 0
        stack = []



        def dfs(point):
            r,c = point
            nonlocal perimeter

            if point in visited:
                return

            if point not in visited:
                visited.add(point)

            # check up
            if r-1 < 0:
                perimeter += 1
            else:
                if grid[r-1][c] == 0:
                    perimeter += 1
                else:
                    if (r-1,c) not in visited:
                        dfs((r-1,c))

            # check right
            if c + 1 >= cols:
                perimeter += 1
            else:
                if grid[r][c+1] == 0:
                    perimeter += 1
                else:
                    if (r, c+1) not in visited:
                        dfs((r, c+1))

            # check down
            if r+1 >= rows:
                perimeter += 1
            else:
                if grid[r + 1][c] == 0:
                    perimeter += 1
                else:
                    if (r + 1, c) not in visited:
                        dfs((r + 1, c))

            # check left
            if c-1 < 0:
                perimeter += 1
            else:
                if grid[r][c-1] == 0:
                    perimeter += 1
                else:
                    if (r, c-1) not in visited:
                        dfs((r, c-1))


        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    dfs((i,j))

        return perimeter

# leetcode submit region end(Prohibit modification and deletion)
