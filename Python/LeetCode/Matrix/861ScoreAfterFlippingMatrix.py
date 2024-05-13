class Solution:
    def matrixScore(self, grid: list[list[int]]) -> int:
        score = 0
        for r in range(len(grid)):
            if grid[r][0] == 0:
                self.flip(grid[r])

        for c in range(len(grid[0])):
            if sum(grid[r][c] for r in range(len(grid))) < len(grid) / 2:
                self.flip_column(grid, c)

        score = self.calcScore(grid)
        return score

    def flip(self, vector):
        for i in range(len(vector)):
            vector[i] = 1 - vector[i]

    def flip_column(self, grid, col):
        for r in range(len(grid)):
            grid[r][col] = 1 - grid[r][col]

    def calcScore(self, grid):
        score = 0
        for row in grid:
            score += int(''.join(map(str, row)), 2)
        return score


print(Solution().matrixScore(grid=[[0, 0, 1, 1], [1, 0, 1, 0], [1, 1, 0, 0]]))
