"""
Input: grid = [[2,5,4],[1,5,1]]
Output: 4

"""
import math
class Solution:
    def gridGame(self, grid: list[list[int]]) -> int:
        n = len(grid[1])
        left=0
        right=sum(grid[0])
        result = math.inf
        for i in range(n):
            right -=grid[0][i]
            result = min(result,max(left,right))
            left +=grid[1][i]
        return result

# grid = [[3,3,1],[8,5,2]]
# grid = [[1,3,1,15],[1,3,3,1]]
grid =[[20,3,20,17,2,12,15,17,4,15],
       [20,10,13,14,15,5,2,3,14,3]]
print(Solution().gridGame(grid))
