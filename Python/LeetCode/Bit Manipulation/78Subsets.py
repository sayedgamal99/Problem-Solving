# 1- bit manipulation solution:

class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        answer = []
        n = len(nums)
        for i in range(1 << n):
            s = []
            for j in range(n):
                if (i & (1 << j)) != 0:
                    s.append(nums[j])
            answer.append(s)
        return answer


# 2- backtracking solution:

class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:

        result = []
        res = []

        def dfs(i):
            if i == len(nums):
                result.append(res.copy())
                return

            res.append(nums[i])
            dfs(i+1)
            res.pop()
            dfs(i+1)
        dfs(0)
        return result
