# Complexity:
# Time O(n): we traverse the list of prices once.
# Space O(n): we use a 2D array to store the maximum profit
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0] * n for _ in range(2)] #dp[i,j] is max earning in at most i + 1 transactions on j price


        # dp[0][k] is the best earning with 1 transaction at position k, 
        # The transaction could posibly end before position k
        # dp[0][n-1] is the best earning with just 1 position
        min_price = prices[0]
        for j in range(1, n):
            min_price = min(min_price, prices[j])
            dp[0][j] = max(
                dp[0][j-1], # do nothing and get the previous earning
                prices[j]- min_price # buy at min and sell now
            )

        # dp[1][k] is the best earning with 2 transactions at position k,
        # To calculate it we use the formula dp[1][k] = max( dp[0][j] + price[k] - price[j], j=0:k-1 )
        # We dont need a double loop to check each j because when we calculated k, if we want to calculate k+1 we just need to add the
        # new difference to previous best calculation and add the new calculation for j = k
        # The best earning of two position is the maximum value of the array dp[1].
        for j in range(1,n):
            new_diff = prices[j] - prices[j-1]
            dp[1][j] = max(
                dp[0][j-1] + new_diff, # open at last previous price an close now
                dp[1][j-1] + new_diff # contains the best of other previous calculations, just need to add the recent difference
            )

        return max(dp[0][n-1], max(dp[1])) # max of one or two transactions