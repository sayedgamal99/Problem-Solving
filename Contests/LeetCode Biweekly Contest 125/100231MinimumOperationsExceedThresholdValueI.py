class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        answer = 0
        for item in nums:
            if item< k:
                answer+=1
        return answer

print(Solution().minOperations(nums = [2, 11,10,1,3], k = 10))