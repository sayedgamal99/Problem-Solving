class Solution:
    def checkValidString(self, s: str) -> bool:
        leftmin, leftmax = 0, 0
        for c in s:
            if c == '(':
                leftmax += 1
                leftmin += 1
            elif c == ')':
                leftmax -= 1
                leftmin -= 1
            else:
                leftmin -= 1
                leftmax += 1
            if leftmax < 0:
                return False
            if leftmin < 0:
                leftmin = 0
            return leftmin == 0


my_incomplete_solution = """class Solution:
    def checkValidString(self, s: str) -> bool:
        stack = []
        ast = 0
        diff = 0
        for r in range(len(s)):
            if s[r] == '(':
                stack.append(s[r])
                diff += 1
            elif s[r] == ')':
                if stack:
                    stack.pop()
                elif ast:
                    ast -= 1
                    diff+=1
                else:
                    return False
            else:
                ast += 1
                diff -= 1
        # print(stack, ast)
        if not stack:
            return True
        print('dd', diff)
        return True if (ast - len(stack)) >= 0 and diff > 0 else False


print(Solution().checkValidString(s="(*))"))
print(Solution().checkValidString(s="((*)"))
print(Solution().checkValidString(s="(*)"))
print(Solution().checkValidString(
    "(((((()*)(*)*))())())(()())())))((**)))))(()())()"))
print(Solution().checkValidString(
    s="((((()(()()()*()(((((*)()*(**(())))))(())()())(((())())())))))))(((((())*)))()))(()((*()*(*)))(*)()"))
print(Solution().checkValidString(
    "(((((*(()((((*((**(((()()*)()()()*((((**)())*)*)))))))(())(()))())((*()()(((()((()*(())*(()**)()(())"))
"""
