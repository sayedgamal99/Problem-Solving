from collections import Counter as co


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        ss = co(s)
        tt = co(t)

        result = 0
        for letter in tt:
            if letter not in ss:
                result += tt[letter]
            else:
                if tt[letter] > ss[letter]:
                    result += (tt[letter]-ss[letter])

        return result


print(Solution().minSteps(s="leetcode", t="practice"))
# print(Solution().minSteps(s="anagram", t="mangaar"))
print(Solution().minSteps(s='bab', t='aba'))


# Another obtimized solution (same idea):

"""
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        
        res = 0
        for i in set(t):
            kk  = t.count(i)-s.count(i) 
            res+= kk if kk>0 else 0
        return res
    
"""
