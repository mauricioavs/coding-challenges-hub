# Complexity:
# Time O(m*n): where m and n are the dimensions of the input matrix.
# Space O(n): memory for the mem list stores the accumulative count of nums in same column.
# For example, If a row has 5 consecutive 1s, then you must have 5 consecutive 1s in the same columns to form a square.
# We iterate through the matrix and for each row, we update the mem list with the accumulative count of 1s in the same column.
# Then we check if we can form a square of size best + 1, if we can, we update the best variable.
# We just search for best + 1, because if we can form a square of size best + 1, then we can form a square of size best in the previous row, and best-1 on the next previous one and so on.
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])

        mem = [0] * n
        best = 0

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == "1":
                    mem[j] += 1
                else:
                    mem[j] = 0

            target = best + 1
            count = 0
            for j in range(n):
                if mem[j] >= target:
                    count += 1
                else:
                    count = 0

                if count == target:
                    best += 1
                    break

        return best* best
