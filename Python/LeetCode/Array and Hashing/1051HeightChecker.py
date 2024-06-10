class Solution:
    def heightChecker(self, heights: list[int]) -> int:
        expected = heights.copy()
        expected.sort()
        answer = 0
        for i in range(len(heights)):
            if heights[i] != expected[i]:
                answer += 1
        return answer
