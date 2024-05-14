class Solution:
    def getMaximumGold(self, grid: list[list[int]]) -> int:
        answer = 0
        row, col = len(grid), len(grid[0])

        def dfs(i, j, current_sum):
            if i < 0 or j < 0 or i >= row or j >= col or grid[i][j] <= 0:
                return current_sum
            # Temporarily mark the cell as visited
            original_value = grid[i][j]
            current_sum += original_value
            grid[i][j] = -1

            # Explore all four directions
            max_sum = max(dfs(i+1, j, current_sum),
                          dfs(i-1, j, current_sum),
                          dfs(i, j+1, current_sum),
                          dfs(i, j-1, current_sum))

            # Backtrack: restore the original value of the cell
            grid[i][j] = original_value

            return max_sum

        for r in range(row):
            for c in range(col):
                if grid[r][c] > 0:
                    answer = max(answer, dfs(r, c, 0))

        return answer


print(Solution().getMaximumGold(grid=[[0, 6, 0], [5, 8, 7], [0, 9, 0]]))  # 24
print(Solution().getMaximumGold(
    [[1, 0, 7], [2, 0, 6], [3, 4, 5], [0, 3, 0], [9, 0, 20]]))  # 28
print(Solution().getMaximumGold([[1, 0, 7, 0, 0, 0], [2, 0, 6, 0, 1, 0], [
      3, 5, 6, 7, 4, 2], [4, 3, 1, 0, 2, 0], [3, 0, 5, 0, 20, 0]]))  # 60
