class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def remove_pair(s, a, b, points):
            stack = []
            score = 0
            for char in s:
                stack.append(char)
                if len(stack) > 1 and stack[-2] == a and stack[-1] == b:
                    score += points
                    stack.pop()
                    stack.pop()
            return ''.join(stack), score

        if x > y:
            s, score = remove_pair(s, 'a', 'b', x)
            _, score2 = remove_pair(s, 'b', 'a', y)
        else:
            s, score = remove_pair(s, 'b', 'a', y)
            _, score2 = remove_pair(s, 'a', 'b', x)

        return score + score2


print(Solution().maximumGain(s="cdbcbbaaabab", x=4, y=5))
print(Solution().maximumGain(s="aabbaaxybbaabb", x=5, y=4))
