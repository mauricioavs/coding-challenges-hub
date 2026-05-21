# Complexity:
# Time O(n): where n is the length of the input list. We compute the solution for each index at most twice.
# Space O(n): memory for the mem dictionary stores the results for all the possible indices, which are near n.
# Same solution as problem 198 but we need to do it twice, one for the case where we dont rob the first house and another for the case where we dont rob the last house. We return the best of both cases.
class Solution:
    def rob(self, nums: List[int]) -> int:
        def solve(i):
            if i >= n:
                return 0

            if i in mem:
                return mem[i]

            rob_current = new_nums[i] + solve(i+2)
            skip_current = solve(i+1)

            mem[i] = max(rob_current, skip_current)
            return mem[i]

        n = len(nums) - 1

        if n == 0:
            return nums[0]

        new_nums = nums[1:]
        mem = {}
        best = solve(0)
        new_nums = nums[:-1]
        mem = {}
        best = max(best, solve(0))
        return best
