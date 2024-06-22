from collections import defaultdict


class Solution:
    def numberOfSubarrays(self, nums: list[int], k: int) -> int:
        count = defaultdict(int) # counts how many sub-arrays with certain number of odd count
        odd_count = 0
        count[0] = 1
        answer = 0
        for r in range(len(nums)):
            if nums[r] % 2:
                odd_count += 1

            if odd_count-k in count:
                answer += count[odd_count-k]

            count[odd_count] += 1

        return answer


print(Solution().numberOfSubarrays(nums=[1, 1, 2, 1, 1], k=3))
print(Solution().numberOfSubarrays([2, 2, 2, 1, 2, 2, 1, 2, 2, 2], 2))
