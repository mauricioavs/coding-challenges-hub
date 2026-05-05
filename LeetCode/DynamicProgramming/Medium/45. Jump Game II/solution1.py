# Complexity:
# Time O(n^2): Two nested loops, total of 1/2 * (n-1) * (n-2) iterations.
# Space O(n): The min_jumps array of size n is used to store the minimum jumps required to reach each index.
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        min_jumps = [n] * n
        min_jumps[0] = 0
        
        for i in range(n):
            for j in range(i):
                available_jumps = nums[j]
                if j + available_jumps >= i:
                    min_jumps[i] = min(min_jumps[i], min_jumps[j] + 1)
        
        return min_jumps[n-1]