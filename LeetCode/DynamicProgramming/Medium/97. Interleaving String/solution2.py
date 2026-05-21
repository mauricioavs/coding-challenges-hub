# Complexity:
# Time O(n1 * n2): We fill a 2D DP table of size (n1 + 1) * (n2 + 1).
# Space O(n1 * n2): The space used by the DP table is (n1 + 1) * (n2 + 1).
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)

        if n1 + n2 != len(s3):
            return False

        dp = [[False] * (n2+1) for _ in range(n1+1) ]

        dp[0][0] = True # "", "" -> ""

        # dp means: can s1[:i] and s2[:j] interleave to form s3[:i+j]

        # use s1 only to form s3[:n1]
        for i in range(1, n1+1):
            dp[i][0] = dp[i-1][0] and s1[i-1] == s3[i-1]

        # use s2 only to form s3[:n2]
        for j in range(1, n2+1):
            dp[0][j] = dp[0][j-1] and s2[j-1] == s3[j-1]

        for i in range(1, n1+1):
            for j in range(1, n2+1):
                dp[i][j] = (
                    dp[i-1][j] and s1[i-1] == s3[i+j-1] # Use s1[i-1] to form s3[i+j-1]
                ) or (
                    dp[i][j-1] and s2[j-1] == s3[i+j-1] # Use s2[j-1] to form s3[i+j-1]
                )

        return dp[n1][n2]