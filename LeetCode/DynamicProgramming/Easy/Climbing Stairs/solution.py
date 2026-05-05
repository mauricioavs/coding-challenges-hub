# Complexity:
# O(n) time: O(n) for loop
# O(n) space: array ways takes O(n) space, other variables take O(1) space
class Solution:
    def climbStairs(self, n: int) -> int:
        ways = [0] * 46

        ways[1] = 1
        ways[2] = 2

        for i in range(3, n+1):
            ways[i] = ways[i-1] + ways[i-2]
        
        return ways[n]