# Complexity:
# Time O(n): Single loop from 1 to n-1 accessing the previous value to update the current value
# Space O(n): We create a list of size n+1 to store the row values
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        n = rowIndex
        row = [1] * (n + 1)

        for k in range(1, n):
            row[k] = row[k-1] * (n-k+1) // k

        return row