# Complexity:
# Time O(n): where n is the length of the input list. We compute the solution for each index at most once.
# Space O(n): memory for the mem dictionary stores the results for all the possible indices, which are near n.
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        mem = {}

        def solve(i):
            if i >= n:
                return 0

            if i in mem:
                return mem[i]

            rob_current = nums[i] + solve(i+2)
            skip_current = solve(i+1)

            mem[i] = max(rob_current, skip_current)
            return mem[i]

        return solve(0)
