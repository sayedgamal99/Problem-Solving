class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:

        l, r = 0, len(matrix)
        answer1 = -1
        while l <= r and l < len(matrix):
            m = (l+r)//2
            if matrix[m][-1] < target:
                l = m+1
            elif matrix[m][-1] > target:
                if matrix[m][0] > target:
                    r = m-1
                else:
                    answer1 = m
                    break
            else:
                return True
        if answer1 == -1:
            return False
        else:
            l, r = 0, len(matrix[m])
            while l <= r:
                m = (l+r)//2
                if matrix[answer1][m] < target:
                    l = m+1
                elif matrix[answer1][m] > target:
                    r = m-1
                else:
                    return True

        return False


test1 = Solution().searchMatrix(matrix=[[1, 3, 5, 7], [
    10, 11, 16, 20], [23, 30, 34, 60]], target=3)
test2 = Solution().searchMatrix(
    matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target=13)
assert test1 == True
assert test2 == False
print('Tests Passed')
