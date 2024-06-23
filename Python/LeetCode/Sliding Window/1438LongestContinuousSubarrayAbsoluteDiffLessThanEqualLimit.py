import heapq
from collections import deque


class Solution:
    def longestSubarray(self, nums: list[int], limit: int) -> int:

        minHeap = []
        maxHeap = []
        n = len(nums)
        l = 0
        answer = 1
        for r in range(n):
            heapq.heappush(minHeap, (nums[r], r))
            heapq.heappush(maxHeap, (-nums[r], r))
            while -maxHeap[0][0] - minHeap[0][0] > limit:
                l += 1
                while minHeap and minHeap[0][1] < l:
                    heapq.heappop(minHeap)
                while maxHeap and maxHeap[0][1] < l:
                    heapq.heappop(maxHeap)
            answer = max(answer, r-l+1)
        return answer


class SolutionMonotonicStacks:
    def longestSubarray(self, nums: list[int], limit: int) -> int:
        maxDeque = deque()
        minDeque = deque()
        l = 0
        answer = 0

        for r in range(len(nums)):
            while maxDeque and nums[r] > maxDeque[-1]:
                maxDeque.pop()
            maxDeque.append(nums[r])

            while minDeque and nums[r] < minDeque[-1]:
                minDeque.pop()
            minDeque.append(nums[r])

            while maxDeque[0] - minDeque[0] > limit:
                if nums[l] == maxDeque[0]:
                    maxDeque.popleft()
                if nums[l] == minDeque[0]:
                    minDeque.popleft()
                l += 1

            answer = max(answer, r - l + 1)

        return answer


print(SolutionMonotonicStacks().longestSubarray(
    nums=[10, 1, 2, 4, 7, 2], limit=5))
