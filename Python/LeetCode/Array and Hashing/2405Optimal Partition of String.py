class Solution:
    def partitionString(self, s: str) -> int:
        theset = set()
        result=0
        for ch in s:
            if ch in theset:
                result+=1
                theset.clear()
            theset.add(ch)

        return result+1

s = 'ssssss'
print(Solution().partitionString(s))