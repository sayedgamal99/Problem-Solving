class Solution:
    def operations(self, operation, t1, t2):
        if operation == '+':
            return t1+t2
        elif operation == '-':
            return t1-t2
        elif operation == '*':
            return t1*t2
        elif operation == '/':
            return int(t1/t2)

    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        for token in tokens:
            if token[1:].isdecimal() or token.isdecimal():
                stack.append(int(token))
            else:
                t2, t1 = stack.pop(), stack.pop()
                stack.append(self.operations(token, t1, t2))
            print(stack, token)
        return stack.pop()


print(Solution().evalRPN(["4", "13", "5", "/", "+"]))
print(Solution().evalRPN(["10", "6", "9", "3", "+",
      "-11", "*", "/", "*", "17", "+", "5", "+"]))
