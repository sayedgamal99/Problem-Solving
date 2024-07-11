class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = ['']
        for char in s:
            if char == '(':
                stack.append('')
            elif char == ')':
                poped = stack.pop()[::-1]
                stack[-1] += poped
            else:
                stack[-1] += char
        return stack[-1]


print(Solution().reverseParentheses("(abcd)"))
print(Solution().reverseParentheses('(u(love)i)'))
print(Solution().reverseParentheses(s="(ed(et(oc))el)"))
