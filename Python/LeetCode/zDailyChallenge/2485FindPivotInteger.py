from math import sqrt


class Solution:
    def sumToElement(self, n):
        return (n*(n+1))//2

    def pivotInteger(self, n: int) -> int:
        for j in range(n, 0, -1):
            currentS = self.sumToElement(j)
            if currentS == (self.sumToElement(n)-currentS+j):
                return j
        return -1


# print(Solution().pivotInteger(8))

# -------------------------------------------------------
# ANOTHER SOLUTION: USING Square root..


class Solution:
    def SquareSumToElement(self, n):
        return sqrt((n*(n+1))//2)

    def pivotInteger(self, n: int) -> int:
        X = self.SquareSumToElement(n)
        return int(X) if int(X) == X else -1


print(Solution().pivotInteger(8))
