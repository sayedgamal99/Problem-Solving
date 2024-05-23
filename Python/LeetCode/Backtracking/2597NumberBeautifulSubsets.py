from collections import defaultdict


class SolutionBackTracking:
    def beautifulSubsets(self, nums: list[int], k: int) -> int:

        def helper(i, count):
            if i == len(nums):
                return 1

            res = helper(i+1, count)

            if not count[nums[i]+k] and not count[nums[i]-k]:
                count[nums[i]] += 1
                res += helper(i+1, count)
                count[nums[i]] -= 1
            return res
        return helper(0, defaultdict(int))-1


class SolutionTLE:
    def beautifulSubsets(self, nums: list[int], k: int) -> int:
        subsets = self.allSubsets(nums)
        subsets = sum([1 for s in subsets if self.isBeaty(s, k)])-1
        return subsets

    def allSubsets(self, nums):
        subsets = []
        n = len(nums)
        for i in range(1 << n):
            s = []
            for j in range(n):
                if (i & 1 << j) != 0:
                    s.append(nums[j])
            subsets.append(s)
        return subsets

    def isBeaty(self, subset, k):
        n = len(subset)
        for i in range(n):
            for j in range(i+1, n):
                if abs(subset[i] - subset[j]) == k:
                    return False
        return True
