# very efficient solution with hashmap:

class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        themap = {}
        for i in range(len(nums)):
            if nums[i] in themap:
                check = (i-themap[nums[i]]) <= k
                if check:
                    return True
            themap[nums[i]] = i

        return False


# Sliding Window Technique with using set
class Solution2:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        slidingW = set()
        l = 0
        for r in range(len(nums)):
            if r-l > k:
                slidingW.remove(nums[l])
                l += 1
            if nums[r] in slidingW:
                return True
            slidingW.add(nums[r])
        return False


print(Solution().containsNearbyDuplicate(nums=[1, 2, 3, 1], k=3))
print(Solution().containsNearbyDuplicate(nums=[2, 2], k=3))
print(Solution().containsNearbyDuplicate(nums=[1, 2, 3, 1, 2, 3], k=2))
print(Solution().containsNearbyDuplicate([4, 1, 2, 3, 1, 5], 3))

print('\n\nSolution(2):\n')

print(Solution2().containsNearbyDuplicate(nums=[1, 2, 3, 1], k=3))
print(Solution2().containsNearbyDuplicate(nums=[2, 2], k=3))
print(Solution2().containsNearbyDuplicate(nums=[1, 2, 3, 1, 2, 3], k=2))
print(Solution2().containsNearbyDuplicate([4, 1, 2, 3, 1, 5], 3))
