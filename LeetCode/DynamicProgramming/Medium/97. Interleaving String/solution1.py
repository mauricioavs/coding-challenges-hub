# Complexity:
# Time O(n1 * n2): Each state (i, j) is computed at most once (memorization). There are (n1 + 1) * (n2 + 1) possible states.
# Space O(n1 * n2): The space used by the memoization dictionary can grow up to (n1 + 1) * (n2 + 1) in the worst case.
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)
        n3 = len(s3)
        
        if n1 + n2 != n3:
            return False

        mem = {}

        def solve(i: int, j: int) -> bool:
            if (i, j) in mem:
                return mem[(i, j)]

            k = i + j

            if k == n3:
                return True

            take_s1 = False
            take_s2 = False

            if i < n1 and s1[i] == s3[k]:
                take_s1 = solve(i+1, j)

            if j < n2 and s2[j] == s3[k]:
                take_s2 = solve(i, j+1)

            mem[(i, j)] = take_s1 or take_s2
            return mem[(i, j)]

        return solve(0, 0)
        