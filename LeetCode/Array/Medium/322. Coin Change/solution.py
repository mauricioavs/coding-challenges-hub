# Complexity:
# Time: O(n * m): We iterate through each amount from 1 to amount (n) and for each amount, we iterate through the coins (m).
# Space: O(n): We use an array of size amount + 1 to store the minimum coins needed for each amount.
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        nums = [float("inf")] * (amount + 1)
        nums[0] = 0

        for amt in range(1, amount + 1):
            for coin in coins:
                if amt >= coin:
                    nums[amt] = min(nums[amt - coin] + 1, nums[amt])

        return nums[-1] if nums[-1] != float("inf") else -1
