class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        child = 0
        co = 0
        g.sort()
        s.sort()
        while(co<len(s) and child<len(g)):
            if g[child]<=s[co]:
                child+=1
            co+=1

        return child
    

# print(Solution().findContentChildren([1, 2, 3], [1, 1]))
print(Solution().findContentChildren([1, 2], [1,2,3]))