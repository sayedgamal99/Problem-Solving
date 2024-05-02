class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums.sort()
        l, r = 0, len(nums)-1
        while l <= r:
            if nums[l] < 0 and nums[r] > 0:
                nl, nr = abs(nums[l]), abs(nums[r])
                if nl != nr:
                    if nl < nr:
                        r -= 1
                    else:
                        l += 1
                else:
                    return nr
            else:
                return -1
