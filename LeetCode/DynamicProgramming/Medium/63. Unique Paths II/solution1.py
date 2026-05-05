# Complexity:
# Time O(m*n): We need to iterate through each cell in the grid once to compute the number of unique paths.
# Space O(1): We are modifying the input grid in place.
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])

        for i in range(m):
            for j in range(n):
                # Is better tu put obstacles as 0 and free cells as 1,
                # because we can use direct formula grid[i][j] = grid[i-1][j] + grid[i][j-1] to calculate the number of paths to reach each cell
                if obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = 0
                    continue
                    
                obstacleGrid[i][j] = 1

                if i == 0 and j == 0:
                    continue
                elif i == 0:
                    obstacleGrid[0][j] = obstacleGrid[0][j-1]
                elif j == 0:
                    obstacleGrid[i][0] = obstacleGrid[i-1][0]
                else:
                    obstacleGrid[i][j] = obstacleGrid[i-1][j] + obstacleGrid[i][j-1]
        
        return obstacleGrid[m-1][n-1]
