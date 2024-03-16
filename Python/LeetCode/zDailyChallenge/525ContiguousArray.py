class Solution:
    def findMaxLength(self, nums: list[int]) -> int:
        themap = {0: -1}
        answer = 0
        zeros, ones = 0, 0
        for r in range(len(nums)):
            if nums[r]:
                ones += 1
            else:
                zeros += 1

            diff = ones-zeros
            if diff not in themap:
                themap[diff] = r
            else:
                answer = max(answer, r-themap[diff])
                # print(r,diff,themap[diff],answer)
        return answer


print(Solution().findMaxLength(nums=[0, 1, 0]))
print(Solution().findMaxLength(nums=[1, 0, 1, 1, 1, 1, 0, 0]))
