"""
class Solution:
    def sortColors(self, nums: list[int]) -> None:
        def merge(nums,l,h,m):
            L=nums[l:m+1]
            R=nums[m+1:h+1]
            i,j,k=0,0,l
            while(i<len(L) and j<len(R)):
                if L[i]<=R[j]:
                    nums[k]=L[i]
                    i+=1
                else:
                    nums[k]=R[j]
                    j+=1
                k+=1
            while(i<len(L)):
                nums[k]=L[i]
                i+=1
                k+=1
            while(j<len(R)):
                nums[k]=R[j]
                j+=1
                k+=1
            return nums
        def merge_sort(nums,l,h):
            if l==h:
                return nums
            else:
                m=(l+h)//2
            merge_sort(nums,l,m)
            merge_sort(nums,m+1,h)
            merge(nums,l,h,m)
            return nums
        merge_sort(nums, 0, len(nums)-1)
"""
"""
pretty good solution below>>>>>
"""
class Solution:
    def sort_colors(self,nums):
        numbers = [0]*3
        for i in nums:
            numbers[i]+=1
        nums = [0]*numbers[0]+[1]*numbers[1]+[2]*numbers[2]
        return nums

numss = [0, 1, 2, 0, 0, 2, 1, 2, 1]
print(Solution().sort_colors(nums=numss))
# print(numss)