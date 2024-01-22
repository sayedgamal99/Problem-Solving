class Solution:
    def arraySign(self, nums: list[int]) -> int:
        neg_count = 0
        for number in nums:
            if number<0: neg_count+=1
            elif number==0: return 0
        return 1 if neg_count%2 == 0 else  -1
    

nums = [-1,-2,-3,-4,3,2,1]
print(Solution().arraySign(nums))