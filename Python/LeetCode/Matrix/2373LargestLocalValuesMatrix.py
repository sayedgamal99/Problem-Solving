class Solution:
    def largestLocal(self, grid: list[list[int]]) -> list[list[int]]:
        n = len(grid)
        max_pooling = [[0 for _ in range(n-2)] for _ in range(n-2)]
        for i in range(n-2):
            for j in range(n-2):
                maxi = float('-inf')
                for x in range(3):
                    for y in range(3):
                        maxi = max(maxi, grid[i+x][j+y])
                max_pooling[i][j] = maxi
        return max_pooling


print(Solution().largestLocal(
    grid=[[9, 9, 8, 1], [5, 6, 2, 6], [8, 2, 6, 4], [6, 2, 2, 2]]))
