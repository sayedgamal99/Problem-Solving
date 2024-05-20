class Solution:
    def subsetXORSum(self, nums: list[int]) -> int:
        answer = 0
        n = len(nums)

        # generate all subsets of the array using bit manipulation
        for i in range(1 << n):  # 2^n
            s = 0
            for j in range(n):
                if (i & (1 << j)) != 0:  # to discover ones exited to add
                    s ^= nums[j]
            answer += s
        return answer

# with backtracking:


class SolutionB:
    def subsetXORSum(self, nums: list[int]) -> int:
        def dfs(i, total):
            if i == len(nums):
                return total

            return dfs(i+1, total ^ nums[i]) + dfs(i+1, total)
        return dfs(0, 0)


print(Solution().subsetXORSum(nums=[3, 4, 5, 6, 7, 8]))  # 480
print(Solution().subsetXORSum(nums=[5, 1, 6]))  # 28
