# Complexity:
# Time O(n1 * n2): we iterate throuhg(n1 + 1) * (n2 + 1) states
# Space O(n2): The space uses one row of the DP table at a time, which has a size of (n2 + 1).
# This solution is an optimization of soluition2.
# The idea is to store one row of the DP table at a time, since we only need the previous row to compute the current row.
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)

        if n1 + n2 != len(s3):
            return False

        dp = [False] * (n2+1)

        dp[0] = True

        for j in range(1, n2+1):
            dp[j] = dp[j-1] and s2[j-1] == s3[j-1]

        for i in range(1, n1+1):
            dp[0] = dp[0] and s1[i-1] == s3[i-1]
            for j in range(1, n2+1):
                dp[j] = (
                    dp[j] and s1[i-1] == s3[i+j-1]
                ) or (
                    dp[j-1] and s2[j-1] == s3[i+j-1]
                )
        
        return dp[n2]