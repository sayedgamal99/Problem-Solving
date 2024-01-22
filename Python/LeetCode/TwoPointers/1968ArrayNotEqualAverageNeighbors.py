class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:

        i = 1
        while i < len(nums)-1:

            if nums[i] == (nums[i-1]+nums[i+1])/2:
                print(nums, i, nums[i],'___1')

                nums[i],nums[i+1] = nums[i+1],nums[i]
                print(nums,i,nums[i])
                i-=2
            i+=1
            

        return nums


print(Solution().rearrangeArray([1, 2, 3, 4, 5]))
print(Solution().rearrangeArray([3,2,1]))
print('new')
print(Solution().rearrangeArray([10, 7, 5, 4, 3]))
print('new')

print(Solution().rearrangeArray([2, 6, 8, 9, 10]))
