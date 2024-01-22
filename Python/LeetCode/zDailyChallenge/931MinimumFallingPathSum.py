class Solution:
    def minFallingPathSum(self, matrix: list[list[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        cach = [[-1]*cols for _ in range(rows)]

        def path(i, j):
            if i == rows:
                return 0

            if cach[i][j] != -1:
                return cach[i][j]

            b = path(i + 1, j - 1) if j - 1 >= 0 else float('inf')
            a = path(i + 1, j)
            c = path(i + 1, j + 1) if j + 1 <= rows - 1 else float('inf')

            cach[i][j] = min(a, b, c)+matrix[i][j]
            # print(i, j)

            return cach[i][j]

        result = min(path(0, j) for j in range(cols))
        return result


print(Solution().minFallingPathSum(matrix=[[2, 1, 3], [6, 5, 4], [7, 8, 9]]))
print(Solution().minFallingPathSum(
    [[100, -42, -46, -41], [31, 97, 10, -10], [-58, -51, 82, 89], [51, 81, 69, -51]]))


# better solution (DB):
class Solution:
    def minFallingPathSum(self, matrix: list[list[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])

        dp = [[0] * cols for _ in range(rows)]
        dp[0] = matrix[0][:]

        for i in range(1, rows):
            for j in range(cols):
                left = dp[i - 1][j - 1] if 0 <= j - 1 < cols else float('inf')
                up = dp[i - 1][j]
                right = dp[i - 1][j + 1] if 0 <= j + 1 < cols else float('inf')

                dp[i][j] = matrix[i][j] + min(left, up, right)

        return min(dp[rows - 1])
