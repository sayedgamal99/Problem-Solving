class Solution:
    def missingInteger(self, nums: list[int]) -> int:
        summ = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]+1:
                summ += nums[i]
            else:
                sett = set(nums)
                xx = 0
                # print(i,summ)
                for j in range(summ, max(sett)+summ):
                    if j not in sett:
                        return j
                    
                    xx = j
                    # print(xx)

                return xx+1
        return summ+1


# print(Solution().missingInteger([3,4,5,1,12,14,13]))
print(Solution().missingInteger([1, 2, 3, 2, 5]))
