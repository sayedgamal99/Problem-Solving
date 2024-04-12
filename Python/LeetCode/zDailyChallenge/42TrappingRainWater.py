
# two pointers solution
class Solution2:
    def trap(self, height: list[int]) -> int:
        maxleft = [0]
        for i in range(1, len(height)):
            maxleft.append(max(maxleft[-1], height[i-1]))
        maxright = [0]
        for i in range(len(height)-2, -1, -1):
            maxright.append(max(maxright[-1], height[i+1]))
        maxright.reverse()
        result = 0
        for i, h in enumerate(height):
            T = (min(maxleft[i], maxright[i])-h)
            result += T if T > 0 else 0
        return result


# monotonic decreasing stack
class Solution:
    def trap(self, height: list[int]) -> int:
        stack = []  # decreasing stack
        res = 0
        for i, r in enumerate(height):
            while stack and r > stack[-1][0]:
                bar, _ = stack.pop()
                if stack:
                    l, leftBound = stack[-1][1], stack[-1][0]
                    minBound = min(r, leftBound)
                    res += (i - l - 1) * (minBound - bar)

            stack.append((r, i))
        return res


print(Solution().trap([4, 2, 0, 3, 2, 5]))
print(Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
print(Solution().trap([1, 0, 1]))
