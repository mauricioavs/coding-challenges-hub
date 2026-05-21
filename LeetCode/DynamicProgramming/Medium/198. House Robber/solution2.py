# Complexity:
# Time O(n): where n is the length of the input list. We compute the solution for each index at most once.
# Space O(n): we create a new list of size + 1.
class Solution:
    def rob(self, nums: List[int]) -> int:
        nums = [0] + nums  # we add a 0 at the beginning to iterate the second house (select first or second house for the position of second house)
        for i in range(2, len(nums)):
            # Two options: either we rob the current house or we skip the current house and take the solution of the previous house.
            nums[i] = max(nums[i-1], nums[i-2] + nums[i])

        return nums[-1]