# Complexity:
# Time O(n^2) where n is the number of rows in the triangle
# Space O(n^2) where n is the number of rows in the triangle
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = [[1]]
        for row in range(1, numRows):
            newRow = [1]
            for i in range(1, row):
                newRow.append(triangle[row-1][i-1] + triangle[row-1][i])
            newRow.append(1)
            triangle.append(newRow)

        return triangle