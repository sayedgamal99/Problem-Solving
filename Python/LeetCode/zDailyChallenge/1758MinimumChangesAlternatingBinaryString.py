class Solution:
    def minOperations(self, s: str) -> int:
        s1,s0 = 0,0
        for i in range(len(s)):

            if i%2==0:
                if s[i]=='0':
                    s1+=1
                else:
                    s0+=1
            else:
                if s[i]=='0':
                    s0+=1
                else:
                    s1+=1
        return min(s1,s0)


# print(Solution().minOperations('0100'))
# print(Solution().minOperations('01'))
print(Solution().minOperations('10010100'))
# 10010100
# 01010101
