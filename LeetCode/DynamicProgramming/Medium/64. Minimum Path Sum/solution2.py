# Complexity:
# Time O(m*n): We need to iterate through each cell in the grid once to compute the minimum path sum.
# Space O(n): We are using a dp array of size n to store the minimum path
# This is faster than solution1.
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n =len(grid), len(grid[0])

        dp = [0] * n
        dp[0] = grid[0][0]

        # Initialize the first row of the dp array with accumulated sums from the first row of the grid
        for i in range (1, n):
            dp[i] = dp[i-1] + grid[0][i]

        for i in range(1, m):
            # Update the first element of the dp array for the current row
            dp[0] += grid[i][0]
            for j in range(1,n):
                dp[j] = min(dp[j-1], dp[j]) + grid[i][j]

        return dp[-1]