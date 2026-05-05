# Complexity:
# Time O(m*n): We need to iterate through each cell in the grid once to compute the minimum path sum.
# Space O(1): We are modifying the input grid in place
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m =len(grid)
        n = len(grid[0])

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                elif i == 0:
                    grid[0][j] += grid[0][j-1]
                elif j == 0:
                    grid[i][0] += grid[i-1][0]
                else:
                    grid[i][j] += min(grid[i-1][j], grid[i][j-1])

        return grid[m-1][n-1]