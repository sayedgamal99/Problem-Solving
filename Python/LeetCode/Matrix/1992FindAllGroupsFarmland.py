class Solution:
    def findFarmland(self, land: list[list[int]]) -> list[list[int]]:
        row, col = len(land), len(land[0])
        NumberOfIslands = 0
        Farm = []

        def dfs(i, j, FarmNumber):
            """
            To Explore each farm recursively and get max right edge and min left edge.
            """
            if i < 0 or j < 0 or i >= row or j >= col or land[i][j] != 1:
                return
            Farm[FarmNumber][0] = min(Farm[FarmNumber][0], i)
            Farm[FarmNumber][1] = min(Farm[FarmNumber][1], j)
            Farm[FarmNumber][2] = max(Farm[FarmNumber][2], i)
            Farm[FarmNumber][3] = max(Farm[FarmNumber][3], j)
            land[i][j] = -1

            for up, right in [[1, 0],  [0, 1]]:
                dfs(i+up, j+right, FarmNumber)

        for i in range(row):
            for j in range(col):
                if land[i][j] == 1:
                    NumberOfIslands += 1
                    Farm.append([999, 999, 0, 0])
                    dfs(i, j, NumberOfIslands-1)
        return Farm


print(Solution().findFarmland([[1, 0, 0], [0, 1, 1], [0, 1, 1]]))
