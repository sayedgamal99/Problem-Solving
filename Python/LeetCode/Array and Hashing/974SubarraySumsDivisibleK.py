class Solution:
    def subarraysDivByK(self, nums, k):
        answer = 0
        count_map = {0: 1}
        s = 0
        for i in range(len(nums)):
            s += nums[i]
            if s % k in count_map:
                answer += count_map[s % k]
            count_map[s % k] = count_map.get(s % k, 0)+1
        return answer


print(Solution().subarraysDivByK(nums=[4, 5, 0, -2, -3, 1], k=5))


class SolutionTLE:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        answer = 0
        n = len(nums)
        for i in range(n):
            s = 0
            for j in range(i, n):
                s += nums[j]
                if s % k == 0:
                    answer += 1
        return answer
