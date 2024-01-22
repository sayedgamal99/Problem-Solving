class NumMatrix:

    def __init__(self, matrix: list[list[int]]):
        ROW,COL=len(matrix),len(matrix[0])

        prfx_matrix = [[0]*(COL+1) for r in range(ROW+1)]

        for r in range(ROW):
            prfx = 0
            for c in range(COL):
                prfx+=matrix[r][c]
                topp_prfx = prfx_matrix[r][c+1]
                prfx_matrix[r+1][c+1]=prfx+topp_prfx
        self.prfx_matrix = prfx_matrix


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        topleft = self.prfx_matrix[row1-1][col1-1]
        left = self.prfx_matrix[row2][col1-1]
        top = self.prfx_matrix[row1-1][col2]
        totalsum = self.prfx_matrix[row2][col2]
        return totalsum-left-top+topleft


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

