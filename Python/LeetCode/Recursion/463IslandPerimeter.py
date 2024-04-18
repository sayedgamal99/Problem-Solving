
# dfs solution
class Solution:
    def islandPerimeter(self, grid):
        answer = 0
        row, col = len(grid), len(grid[0])

        def dfs(i, j):
            if i < 0 or j < 0 or i >= row or j >= col or grid[i][j] == 0:
                return 1
            if grid[i][j] == -1:  # visited
                return 0
            grid[i][j] = -1

            return dfs(i+1, j)+dfs(i-1, j)+dfs(i, j+1)+dfs(i, j-1)
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    answer += dfs(r, c)

        return answer


print(Solution().islandPerimeter(
    [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]))
print(Solution().islandPerimeter([[1]]))
print(Solution().islandPerimeter([[1, 1]]))
