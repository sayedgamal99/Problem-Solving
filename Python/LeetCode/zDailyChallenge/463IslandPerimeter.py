class Solution:
    def islandPerimeter(self, grid) -> int:
        answer = 0

        # padding the matrix
        col = len(grid[0])
        grid = [[0]*col, *grid, [0]*col]

        for i in range(len(grid)):
            grid[i] = [0, *grid[i], 0]

        row, col = len(grid), len(grid[0])

        # counting solution
        for i in range(1, row):
            for j in range(1, col):
                if grid[i][j] == 1:

                    if grid[i+1][j] == 0:
                        answer += 1
                    if grid[i-1][j] == 0:
                        answer += 1
                    if grid[i][j+1] == 0:
                        answer += 1
                    if grid[i][j-1] == 0:
                        answer += 1

        return answer


print(Solution().islandPerimeter(
    [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]))
print(Solution().islandPerimeter([[1]]))
print(Solution().islandPerimeter([[1, 1]]))
