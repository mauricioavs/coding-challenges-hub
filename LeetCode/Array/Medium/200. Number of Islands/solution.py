# Complexity:
# Time: O(m * n): Two for loops. DFS marks visited land as water, preventing revisits.
# Space: O(m * n): We use the same grid to mark visited cells, so in the worst case, we may have to store the entire grid in memory if all cells are land.
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        islands = 0

        def dfs(row: int, col: int) -> None:
            if (
                row < 0 or row >= rows or
                col < 0 or col >= cols or
                grid[row][col] == "0"
            ):
                return

            grid[row][col] = "0"

            dfs(row-1, col)
            dfs(row+1, col)
            dfs(row, col-1)
            dfs(row, col+1)


        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    islands += 1
                    dfs(row, col)

        return islands
