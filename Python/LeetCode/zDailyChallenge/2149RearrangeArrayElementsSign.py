class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        pos, neg = [], []
        for n in nums:
            if n > 0:
                pos.append(n)
            else:
                neg.append(n)
        nums = [0]*len(nums)
        l, r = 0, 0
        for i in range(nums):
            if i % 2 == 0:
                nums[i] = pos[r]
                r += 1
            else:
                nums[i] = neg[l]
                l += 1
