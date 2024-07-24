class Solution:
    def sortJumbled(self, mapping: list[int], nums: list[int]) -> list[int]:
        new = []
        for idx, n in enumerate(nums):
            new.append('')
            for i in str(n):
                new[idx] += str(mapping[int(i)])
            new[idx] = int(new[idx])
        all = sorted(zip(new, nums), key=lambda x: x[0],)
        return [t[1] for t in all]



# optimized version
class Solution:
    def sortJumbled(self, mapping: list[int], nums: list[int]) -> list[int]:
        def map_num(n):
            return int(''.join(str(mapping[int(d)]) for d in str(n)))

        return sorted(nums, key=map_num)


print(Solution().sortJumbled(
    mapping=[8, 9, 4, 0, 2, 1, 3, 5, 7, 6], nums=[991, 338, 38]))  # [338,38,991]
