# Complexity:
# Time: O(n^2): [n-2, n-3, n-4, ... , 1]. For each i, we check at most n-2 jumps, then n-1 jumps, and so on, which sums up to O(n^2).
# Space: O(n): reachable array of size n to keep track of which indices are reachable from the start.
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)

        if n ==1:
            return True
        
        reachable = [False] * n
        reachable[0] = True

        for i in range(n):
            if reachable[i] == False:
                continue

            jumps = nums[i]

            for j in range(1, jumps+1):
                reachable[i+j] = True

                if i + j == n - 1:
                    return True
        
        return False