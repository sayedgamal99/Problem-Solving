class Solution:
    def luckyNumbers(self, matrix: list[list[int]]) -> list[int]:
        minrows = [min(row) for row in matrix]
        maxcols = [max(column) for column in zip(*matrix)]
        return set(minrows) & set(maxcols)
