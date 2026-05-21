# Complexity:
# Time O(n): we traverse the input list twice
# Space O(n): we create two new lists of the same size as the input list.
class Solution:
    def rob(self, nums: List[int]) -> int:
        # you can rob just one house
        if len(nums) <= 3:
            return max(nums)

        # dont rob the first house
        first = [0] + nums[1:]
        # dont rob the last house
        second = [0] + nums[:-1]

        # make same solution as problem 198 for both cases
        for i in range(2, len(first)):
            first[i] = max(first[i-1], first[i-2] + first[i])

        for i in range(2, len(second)):
            second[i] = max(second[i-1], second[i-2] + second[i])

        return max(first[-1], second[-1])