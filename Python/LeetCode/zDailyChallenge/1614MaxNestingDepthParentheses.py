class Solution:
    def maxDepth(self, s: str) -> int:
        counter = 0
        answer = 0
        for r in s:
            if r == '(':
                counter += 1
                answer = max(answer, counter)
            elif r == ')':
                counter -= 1
        return max(answer, counter)
