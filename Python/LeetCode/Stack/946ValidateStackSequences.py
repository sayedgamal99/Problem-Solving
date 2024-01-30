class Solution:
    def validateStackSequences(self, pushed: list[int], popped: list[int]) -> bool:
        stack = []
        i = 0
        for item in pushed:
            stack.append(item)

            while len(stack) != 0 and popped[i] == stack[-1] and i < len(popped):
                stack.pop()
                i += 1
        return len(stack) == 0


print(Solution().validateStackSequences(
    pushed=[1, 2, 3, 4, 5], popped=[4, 5, 3, 2, 1]))
