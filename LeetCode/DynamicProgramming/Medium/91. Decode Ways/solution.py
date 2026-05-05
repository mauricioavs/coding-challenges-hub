# Complexity:
# Time O(n): Each index is computed only once thanks to memoization.
# Space O(n): We use O(n) space for the memo dictionary and up to O(n) recursion stack.
class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        memo = {}

        def solve(i: int) -> int:
            if i == n:
                return 1

            if s[i] == "0":
                return 0

            if i in memo:
                return memo[i]

            ways = solve(i + 1)

            if i + 1 < n and 10 <= int(s[i:i + 2]) <= 26:
                ways += solve(i + 2)

            memo[i] = ways
            return ways

        return solve(0)