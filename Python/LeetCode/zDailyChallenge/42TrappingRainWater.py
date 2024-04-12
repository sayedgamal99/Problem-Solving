class Solution:
    def trap(self, height: list[int]) -> int:
        stack = []  # decreasing stack
        res = 0
        for i, r in enumerate(height):
            while stack and r > stack[-1][0]:
                bar, j = stack.pop()
                if stack:
                    l, leftBound = stack[-1][1], stack[-1][0]
                    minBound = min(r, leftBound)
                    res += (i - l - 1) * (minBound - bar)

            stack.append((r, i))
        return res


print(Solution().trap([4, 2, 0, 3, 2, 5]))
print(Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
print(Solution().trap([1, 0, 1]))
