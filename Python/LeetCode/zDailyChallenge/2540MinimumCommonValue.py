class Solution:
    def getCommon(self, nums1: list[int], nums2: list[int]) -> int:
        left, right = 0, 0
        while left < len(nums1) and right < len(nums2):

            if nums1[left] < nums2[right]:
                left += 1
            elif nums1[left] > nums2[right]:
                right += 1
            else:
                return nums1[left]
        return -1


print(Solution().getCommon(nums1=[1, 2, 3, 6], nums2=[2, 3, 4, 5]))
