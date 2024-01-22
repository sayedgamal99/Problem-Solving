
# two pointer solution
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        L = 1
        for R in range(1, len(nums)):
            if nums[R] != nums[R - 1]:
                nums[L] = nums[R]
                L += 1
        print(nums)
        return L

print(Solution().removeDuplicates([0,0,1,1,2,2]))




# ordered set with dictionary solution:
class Solution2:
    def removeDuplicates(self, nums: list[int]) -> int:
        nums[:] = list(dict.fromkeys(nums))
        k= len(nums)
        return k

# print(Solution2().removeDuplicates([0, 0,1,1,1,2,2,3,3,4]))