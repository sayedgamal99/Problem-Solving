
# 1- Up-Down Solution
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


# 2- Bottom-Up Solution (more optimized and iterative)

class Solution:
    def minFallingPathSum(self, grid: list[list[int]]) -> int:

        n = len(grid)
        memo = [[float('inf')]*n for _ in range(n)]
        for col in range(n):
            memo[n-1][col] = grid[n-1][col]

        for r in range(n-2, -1, -1):
            for c in range(n):
                next_min = float('inf')
                for next_c in range(n):
                    if next_c != c:
                        next_min = min(next_min, memo[r+1][next_c])

                memo[r][c] = grid[r][c] + next_min

        return min(memo[0])


# 3- Bottom-Up solution (iterative) with more optimization:

class Solution:
    def minFallingPathSum(self, grid: list[list[int]]) -> int:
        # Save the size of the square grid
        n = len(grid)

        # Initialize a two-dimensional array to cache the result of each sub-problem
        memo = [[inf] * n for _ in range(n)]

        # Minimum and Second Minimum Column Index
        next_min1_c = None
        next_min2_c = None

        # Base Case. Fill and save the minimum and second minimum column index
        for col in range(n):
            memo[n - 1][col] = grid[n - 1][col]
            if next_min1_c is None or memo[n - 1][col] <= memo[n - 1][next_min1_c]:
                next_min2_c = next_min1_c
                next_min1_c = col
            elif next_min2_c is None or memo[n - 1][col] <= memo[n - 1][next_min2_c]:
                next_min2_c = col

        # Fill the recursive cases
        for row in range(n - 2, -1, -1):
            # Minimum and Second Minimum Column Index of the current row
            min1_c = None
            min2_c = None

            for col in range(n):
                # Select minimum from valid cells of the next row
                if col != next_min1_c:
                    memo[row][col] = grid[row][col] + \
                        memo[row + 1][next_min1_c]
                else:
                    memo[row][col] = grid[row][col] + \
                        memo[row + 1][next_min2_c]

                # Save minimum and second minimum column index
                if min1_c is None or memo[row][col] <= memo[row][min1_c]:
                    min2_c = min1_c
                    min1_c = col
                elif min2_c is None or memo[row][col] <= memo[row][min2_c]:
                    min2_c = col

            # Change of row. Update next_min1_c and next_min2_c
            next_min1_c = min1_c
            next_min2_c = min2_c

        # Return the minimum from the first row
        return memo[0][next_min1_c]


# 4- Bottom-Up Approach with saving only values, indexes of the next row:

class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        # Save the size of the square grid
        n = len(grid)

        # Minimum and Second Minimum Column Index
        next_min1_c = None
        next_min2_c = None

        # Minimum and Second Minimum Value
        next_min1 = None
        next_min2 = None

        # Find the minimum and second minimum from the last row
        for col in range(n):
            if next_min1 is None or grid[n - 1][col] <= next_min1:
                next_min2 = next_min1
                next_min2_c = next_min1_c
                next_min1 = grid[n - 1][col]
                next_min1_c = col
            elif next_min2 is None or grid[n - 1][col] <= next_min2:
                next_min2 = grid[n - 1][col]
                next_min2_c = col

        # Fill the recursive cases
        for row in range(n - 2, -1, -1):
            # Minimum and Second Minimum Column Index of the current row
            min1_c = None
            min2_c = None

            # Minimum and Second Minimum Value of the current row
            min1 = None
            min2 = None

            for col in range(n):
                # Select minimum from valid cells of the next row
                if col != next_min1_c:
                    value = grid[row][col] + next_min1
                else:
                    value = grid[row][col] + next_min2

                # Save minimum and second minimum
                if min1 is None or value <= min1:
                    min2 = min1
                    min2_c = min1_c
                    min1 = value
                    min1_c = col
                elif min2 is None or value <= min2:
                    min2 = value
                    min2_c = col

            # Change of row. Update next_min1_c, next_min2_c, next_min1, next_min2
            next_min1_c = min1_c
            next_min2_c = min2_c
            next_min1 = min1
            next_min2 = min2

        # Return the minimum from the first row
        return next_min1
