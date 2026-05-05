# Complexity:
# O(n^2) time: Populates dp takes O(n^2) states, each one with O(1) time to compute
# O(n^2) space: table dp takes O(n^2) space
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        ans = [0,0]
        # Base case: single characters are palindromes
        for i in range(n):
            dp[i][i] = True
        
        # Base case: check for palindromes of length 2
        for i in range(n-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                ans = [i, i + 1]

        # Fill the dp table for substrings of length 3 and grseater
        # ans is always updated to the longest palindrome found so far
        for diff in range(2, n):
            for i in range(0, n-diff):
                j = i + diff
                if s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] = True
                    ans = [i, j]
        i, j = ans
        return s[i : j + 1]