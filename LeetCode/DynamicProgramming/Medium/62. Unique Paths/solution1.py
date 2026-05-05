# Complexity:
# Time O(m*n): We fill an m x n grid, resulting in m*n iterations.
# Space O(m*n): We use an m x n grid to store the number of unique paths to each cell.
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [ [1] * (n) for _ in range(m) ]

        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] = grid[i-1][j] + grid[i][j-1]
        
        return grid[m-1][n-1]