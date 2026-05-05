# Complexity:
# Time O(m*n): (m-1) * (n-1) iterations to fill the grid
# Space O(n): We use a 1D array of size n to store the number of unique paths to each cell in the current row, which is updated iteratively.
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n # stores the current row of the grid, initialized with 1s since there's only one way to reach any cell in the first row

        for _ in range(1, m):
            for j in range(1, n):
                # for j = 1: 
                #   - row[j-1] = row[0] = 1, which corresponds to the paths from the cell to the left
                #   - row [j] = row[1] ,which corresponds to the paths from the cell above
                # for j = 2:
                #   - row[j-1] = row[1], which corresponds to the paths from the cell to the left, which has been updated in the previous iteration of the inner loop
                #   - row[j] = row[2], which corresponds to the paths from the cell above, which has been updated in the previous iteration of the outer loop
                # ...
                row[j] = row[j] + row[j - 1]

        return row[-1]