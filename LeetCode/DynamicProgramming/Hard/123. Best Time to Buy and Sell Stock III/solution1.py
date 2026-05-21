# Complexity:
# Time O(n): we traverse the list of prices once.
# Space O(1): we use a constant amount of space to store the variables.
from ast import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy1, buy2 = float("inf"), float("inf")
        sell1, sell2 = 0, 0

        for price in prices:
            # This block stores the best transaction we have at the moment
            buy1 = min(buy1, price)
            sell1 = max(sell1, price - buy1)
            # This block stores the best second transaction we have at the moment
            buy2 = min(buy2, price - sell1) # we subtract sell1 from price to consider the profit from the first transaction
            sell2 = max(sell2, price - buy2)
        return sell2