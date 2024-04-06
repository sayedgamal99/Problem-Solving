# two solutions based on stack:

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []  # pair (parentheses, position)
        # 1st loop:
        for r in range(len(s)):
            if s[r] == '(':
                stack.append((s[r], r))
            elif s[r] == ')':
                if stack and stack[-1][0] == '(':
                    stack.pop()
                else:
                    stack.append((s[r], r))
        # 2nd loop:
        j = 0
        new_str = []
        while stack:
            pair = stack.pop(0)
            while j != pair[1]:
                new_str.append(s[j])
                j += 1
            else:
                j += 1

        return "".join(new_str)+s[j:]


# print(Solution().minRemoveToMakeValid(s="lee(t(c)o)de)"))
# print(Solution().minRemoveToMakeValid("a)b(c)d"))
# print(Solution().minRemoveToMakeValid(s="))(("))


# ----------------- another better way to remove unwanted parentheses --------------


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []  # pair (parentheses, position)
        # 1st loop:
        s = list(s)
        for r in range(len(s)):
            if s[r] == '(':
                stack.append((s[r], r))
            elif s[r] == ')':
                if stack and stack[-1][0] == '(':
                    stack.pop()
                else:
                    s[r] = ''
        # 2nd loop:
        new_str = list(s)
        for k, v in stack:
            new_str[v] = ''
        return ''.join(new_str)
