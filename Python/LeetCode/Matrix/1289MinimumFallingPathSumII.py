class Solution:
    def minFallingPathSum(self, grid: list[list[int]]) -> int:

        cache = {}
        n = len(grid)
        if n == 1:
            return grid[0][0]

        def dfs(i, j):
            if i == n-1:
                return grid[i][j]
            if (i, j) in cache:
                return cache[(i, j)]
            next_min = float('inf')
            for next_j in range(n):
                if next_j != j:
                    next_min = min(next_min, dfs(i+1, next_j))
            cache[(i, j)] = grid[i][j]+next_min
            return cache[(i, j)]

        answer = float('inf')
        for col in range(n):
            answer = min(answer, dfs(0, col))
        return answer
