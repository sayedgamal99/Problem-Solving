class Solution:
    def maximalRectangle(self, matrix: list[list[str]]) -> int:

        def largestRectangleArea(heights: list[int]) -> int:
            maxArea = 0
            stack = []
            for i, h in enumerate(heights):
                start = i
                while stack and h < stack[-1][1]:
                    l, bar = stack.pop()
                    maxArea = max(bar*(i-l), maxArea)
                    start = l
                stack.append((start, h))

            for i, h in stack:
                maxArea = max(maxArea, h*(len(heights)-i))
            return maxArea

        result = 0
        R, C = len(matrix), len(matrix[0])
        for r in range(R):
            for c in range(C):
                matrix[r][c] = int(
                    matrix[r][c]) + (int(matrix[r-1][c]) if (r > 0 and int(matrix[r][c])) else 0)

            result = max(result, largestRectangleArea(matrix[r]))
        return result
