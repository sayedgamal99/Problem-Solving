# heap solution (ACCEPTED):
import heapq


class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        heapq.heapify(nums)
        operations = 0
        while len(nums) > 1:
            if nums[0] >= k:
                return operations
            it1, it2 = heapq.heappop(nums), heapq.heappop(nums)
            it = min(it1, it2)*2 + max(it1, it2)
            heapq.heappush(nums, it)
            operations += 1
        return operations


print(Solution().minOperations(nums=[2, 11, 10, 1, 3], k=10))
print(Solution().minOperations([69, 89, 57, 31, 84, 97, 50, 38, 91, 86], 91))
print(Solution().minOperations(nums=[1, 1, 2, 4, 9], k=20))


# brute force solution (TLE):
"""
class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        multiple_answer = 0
        while True:
            answer = 0
            for i in nums:
                if i < k:
                    answer += 1
            if answer == 0:
                return 'True Answer = '+str(multiple_answer)
            nums.sort()
            min1 = nums[0]
            min2 = nums[1]
            nums.append((min(min1, min2)*2)+(max(min1, min2)))
            nums.pop(0)
            nums.pop(0)
            multiple_answer += 1


print(Solution().minOperations(nums=[2, 11, 10, 1, 3], k=10))
print(Solution().minOperations([69, 89, 57, 31, 84, 97, 50, 38, 91, 86], 91))
print(Solution().minOperations(nums=[1, 1, 2, 4, 9], k=20))
"""
