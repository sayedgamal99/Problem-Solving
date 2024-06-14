class Solution:
    def minIncrementForUnique(self, nums: list[int]) -> int:
        nums.sort()
        answer = 0

        for i in range(1, len(nums)):
            if nums[i] <= nums[i-1]:
                inc = nums[i-1] + 1 - nums[i]
                nums[i] += inc
                answer += inc
        return answer


print(Solution().minIncrementForUnique(nums=[3, 2, 1, 2, 1, 7]))


class SolutionFreq:
    def minIncrementForUnique(self, nums: list[int]) -> int:
        Freq = [0]*(10**6+3)

        for i in range(len(nums)):
            Freq[nums[i]] += 1

        answer = 0
        for i in range(len(Freq)-1):
            Freq[i+1] += (Freq[i]-1) if Freq[i] > 0 else 0
            answer += (Freq[i]-1) if Freq[i] > 1 else 0
        return answer


print(SolutionFreq().minIncrementForUnique(nums=[3, 2, 1, 2, 1, 7]))
