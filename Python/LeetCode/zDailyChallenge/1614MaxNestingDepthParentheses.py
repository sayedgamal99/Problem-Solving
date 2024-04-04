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


print(Solution().maxDepth(s="(1+(2*3)+((8)/4))+1"))
print(Solution().maxDepth(s="(1)+((2))+(((3)))"))
print(Solution().maxDepth("8*((1*(5+6))*(8/6))"))
