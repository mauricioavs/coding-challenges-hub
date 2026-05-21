# Complexity:
# Time O(n): We traverse the list of prices once
# Space O(1): We use only a constant amount of space to store the last low price and the total earnings
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        last_low = prices[0]
        earnings = 0

        for price in prices[1:]:
            if price > last_low:
                earnings+= price - last_low

            last_low = price

        return earnings