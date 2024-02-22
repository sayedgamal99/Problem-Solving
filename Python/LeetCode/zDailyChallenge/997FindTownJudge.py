class Solution:
    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        if n == 1:
            return 1
        themap = {}
        people = set()
        for j in trust:
            themap[j[1]] = themap.get(j[1], 0)+1
            people.add(j[0])
        for k, v in themap.items():
            if v == n-1 and k not in people:
                return k
        return -1


# print(Solution().findJudge(n=3, trust=[[1, 3], [2, 3], [3, 1]]))
# print(Solution().findJudge(n=3, trust=[[1, 2], [2, 3]]))
print(Solution().findJudge(n=3, trust=[[1, 3], [2, 3]]))

# print(Solution().findJudge(n=3, trust=[
#       [1, 3], [1, 4], [2, 3], [2, 4], [4, 3]]))#3
