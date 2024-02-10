class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if s[i] != ']':
                stack.append(s[i])
            else:
                res = []
                while stack[-1] != '[':
                    res.append(stack.pop())
                else:
                    res.reverse()
                    stack.pop()
                    number = ''
                    while stack and stack[-1].isdigit():
                        number = stack.pop()+number
                    stack.append(int(number)*''.join(res))

        return ''.join(stack)


print(Solution().decodeString('3[a]2[bc]'))
print(Solution().decodeString("2[abc]3[cd]ef"))
print(Solution().decodeString("3[a2[c]]"))  # 3acc
print(Solution().decodeString('3[sayed]'))
print(Solution().decodeString('100[leetcode]'))
