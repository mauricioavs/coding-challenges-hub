# Complexity:
# Time: O(n*m*k) where n is the length of the string, m is the number of words in the dictionary and k is the average length of the words in the dictionary.
# Space: O(n) where n is the length of the string.
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n+1)

        dp[0] = True

        for i in range(n):
            if dp[i] == False:
                continue

            for word in wordDict:
                if s.startswith(word, i):
                    dp[i+len(word)] = True

        return dp[n]