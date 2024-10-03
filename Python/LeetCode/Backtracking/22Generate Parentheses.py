class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        answers = []
        length = 2*n

        def gen(current, left, right):
            if (right > left) or ((right+left) > length) or ((right+left) == length and right != left):
                return
            elif (right+left == length):
                answers.append(current)
                return
            gen(current+'(', left+1, right)
            gen(current+')', left, right+1)
        gen('', 0, 0)
        return answers


assert Solution().generateParenthesis(n=3) == [
    "((()))", "(()())", "(())()", "()(())", "()()()"]
assert Solution().generateParenthesis(1) == ['()']
print('Tests Passed')


# optimized and simplified code :

class Solution_simplified:
    def generateParenthesis(self, n: int) -> list[str]:
        answers = []

        def backtrack(current, left, right):
            if len(current) == 2 * n:
                answers.append(current)
                return
            if left < n:
                backtrack(current + '(', left + 1, right)
            if right < left:
                backtrack(current + ')', left, right + 1)

        backtrack('', 0, 0)
        return answers
