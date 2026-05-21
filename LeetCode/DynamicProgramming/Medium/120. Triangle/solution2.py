# Complexity:
# Time O(n^2): where n is the number of levels in the triangle.
# Space O(n): We use an additional array of size n to store the minimum path sums for the current level.
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = triangle[-1][:]
        n = len(triangle)

        # We process the triangle from bottom to top.
        # dp starts as the last row. At each upper row, we only update the positions
        # that exist in that row. Since each upper row is shorter, the usable part of
        # dp gets smaller over time (1 space smaller each row): first we update many positions, then fewer, until
        # finally only dp[0] is updated. The remaining values at the end of dp are ignored.
        for row in range(n-2, -1, -1):
            for i in range(row+1):
                dp[i] =  triangle[row][i] + min(dp[i], dp[i+1])

        return dp[0]