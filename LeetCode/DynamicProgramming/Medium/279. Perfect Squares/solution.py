# Complexity:
# Time O(n*sqrt(n)): where n is the input number. We iterate through all numbers from 1 to n, and for each number, we iterate through all perfect squares less than or equal to that number.
# Space O(n): memory for the dp list
class Solution:
    def numSquares(self, n: int) -> int:
        perfect_squares = [i**2 for i in range( 10**2 + 1) if i**2 <= n]

        dp = [float("inf")] * (n+1)

        dp[0] = 0

        for x in range(1, n+1):
            for sq in perfect_squares:
                if sq > x:
                    break
                dp[x] = min(dp[x], dp[x-sq] + 1)

        return dp[n]
