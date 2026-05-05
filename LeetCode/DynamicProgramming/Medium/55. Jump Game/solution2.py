# Complexity:
# Time: O(n): We iterate through the array once, checking each index to see if it can reach the current goal.
# Space: O(1): We use only constant variables.
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums)-1

        for i in range(len(nums)-2,-1,-1):
            # If the current index can reach the goal, then new goal is the current index
            if nums[i] >= (goal-i):
                goal = i

        return True if not goal else False
