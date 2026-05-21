# Complexity:
# Time O(n): We traverse the list of prices once to find the best minimum price and the best difference
# Space O(1): We use only a constant amount of space to store the best minimum price and the best difference
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best_min = prices[0]
        best_diff = 0

        for price in prices[1:]:
            if price < best_min:
                best_min = price
            else:
                best_diff = max(best_diff, price - best_min)

        return best_diff