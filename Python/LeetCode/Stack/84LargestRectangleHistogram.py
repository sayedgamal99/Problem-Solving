class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
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


print(Solution().largestRectangleArea([2, 1, 5, 6, 2, 3]))
