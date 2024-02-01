class Solution:
    def divideArray(self, nums: list[int], k: int) -> list[list[int]]:
        nums.sort()
        result = []
        for i in range(0, len(nums), 3):
            new = nums[i:i+3]
            if (new[-1]-new[0]) > k:
                return []
            else:
                result.append(new)
        return result