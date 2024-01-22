class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        left=0
        right = 1
        while(left<len(nums) and right<len(nums)):
            if nums[left]==0:
                if nums[right]!=0:
                    nums[left],nums[right] = nums[right],nums[left]
                else:
                    right+=1
            else:
                left+=1
                right+=1

        print(nums)



# Solution().moveZeroes([0, 1,0,3,12,0])
Solution().moveZeroes([4, 2,4,0,0,3,0,5,1,0])