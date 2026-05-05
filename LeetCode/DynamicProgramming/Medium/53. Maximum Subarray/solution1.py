# Complexity:
# O(n) time: O(n) for loop
# O(1) space: variables curr_sum and max_sum take O(1) space
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum = nums[0]
        max_sum = nums[0]
        for num in nums[1:]:
            # if curr_sum + num is less than num, then we start a new subarray from num
            curr_sum = max(num, curr_sum + num)
            max_sum = max(curr_sum, max_sum)

        return max_sum