class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        NumberOfIslands = 0
        row, col = len(grid), len(grid[0])

        def dfs(i, j):  # to explore each island and mark it is visited
            if i < 0 or j < 0 or i >= row or j >= col or grid[i][j] != '1':
                return
            grid[i][j] = '-1'
            for up, right in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                dfs(i+up, j+right)

        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1':
                    NumberOfIslands += 1
                    dfs(i, j)
                    print(grid)

        return NumberOfIslands


print(Solution().numIslands(grid=[
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]))
