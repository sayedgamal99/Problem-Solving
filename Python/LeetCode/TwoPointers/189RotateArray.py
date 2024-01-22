# class Solution:
#     def rotate(self, nums: list[int], k: int) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         temp = [0]*len(nums)
#         for i in range(len(nums)): 
#             temp[(i+k)%len(nums)]=nums[i]

#         nums[:] = temp[:]
#         return nums


# solution without extra memory:
class Solution2:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(l=0,r=len(nums)-1):
            while(l<r):
                nums[l], nums[r] = nums[r], nums[l]
                l+=1
                r-=1

        reverse()
        print(nums)

        reverse(0,k-1)
        print(nums)

        reverse(k,len(nums)-1)

        print(nums)








# print(Solution().rotate([1, 2, 3, 4, 5, 6, 7], 3))
print(Solution2().rotate([-1, -100, 3, 99],2))

# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]