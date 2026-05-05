# Complexity:
# Time O(m*n): We iterate through the DP table of size (m+1) x (n+1).
# Space O(m*n): We use a DP table of size (m+1) x (n+1).
# dp[i][j] represents the minimum edit distance between the first i characters of word1 and the first j characters of word2.
# i.e., converting word1[:i] to word2[:j].
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m + 1):
            dp[i][0] = i
        
        for j in range(n + 1):
            dp[0][j] = j

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] # New characters are the same, so no additional edit is needed
                else:
                    dp[i][j] = 1 + min(
                        dp[i][j - 1],      # insert in word1: convert word1[:i] to word2[:j-1] and insert word2[j-1]
                        dp[i - 1][j],      # delete from word1: delete word1[i-1] and convert word1[:i-1] to word2[:j]
                        dp[i - 1][j - 1]   # replace in word1: replace word1[i-1] with word2[j-1], then solve the remaining prefixes word1[:i-1] -> word2[:j-1]
                    )

        return dp[m][n]