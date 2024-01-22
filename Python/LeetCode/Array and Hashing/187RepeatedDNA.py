class Solution:
    def findRepeatedDnaSequences(self, s: str) -> list[str]:
        answer,dnas = set(),set()
        n = len(s)
        for l in range(n-9):
            c = s[l:l+10]
            if c in dnas:
                answer.add(c)
            else:
                dnas.add(c)
        return  list(answer)


ss = input()
print(Solution().findRepeatedDnaSequences(ss))

