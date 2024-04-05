class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        i = 0
        while i < len(s):
            if stack and (ord(stack[-1]) == (ord(s[i])+32) or (ord(stack[-1])+32) == ord(s[i])):
                stack.pop()
                i += 1
                continue
            stack.append(s[i])
            i += 1
        return ''.join(stack)
