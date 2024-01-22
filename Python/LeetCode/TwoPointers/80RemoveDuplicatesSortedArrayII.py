
# two pointer solution
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        L = 1
        for R in range(1, len(nums)):
            print(nums[R])
            if nums[R] != nums[R - 1]:
                nums[L] = nums[R]
                L += 1
            print(nums,L,R)
        return L


print(Solution().removeDuplicates([0, 0, 1, 1, 2, 2]))


# dictionary solution:
from collections import Counter as CO
class Solution2:
    def removeDuplicates(self, nums: list[int]) -> int:
        themap = CO(nums)
        for number in themap:
            if themap[number]>2:
                themap[number]=2
        i=0
        print(themap)
        for number in themap:
            if themap[number]==2:
                nums[i]=number
                nums[i+1] = number
                i+=1
            else:
                nums[i]=number
            i+=1
        print(i)



# print(Solution2().removeDuplicates([0, 0,1,1,1,2,2,3,3,4]))
