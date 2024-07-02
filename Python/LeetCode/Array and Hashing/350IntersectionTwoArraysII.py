from collections import Counter


class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        nums1 = Counter(nums1)
        nums2 = Counter(nums2)

        intersection = nums1 & nums2

        return intersection.elements()
