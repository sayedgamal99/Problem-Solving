class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        ar1,ar2 = set(nums1),set(nums2)
        return [list(ar1-ar2),list(ar2-ar1)]
    
nums1 = [1,2,3]
nums2 = [2,4,6]
print(Solution().findDifference(nums1,nums2))