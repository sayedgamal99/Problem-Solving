class Solution:
    def countSubarrays(self, nums: list[int], minK: int, maxK: int) -> int:
        l = 0
        themap = {'min index': 0,
                  'min value': nums[0], 'max index': 0, 'max value': nums[0]}
        answer = 0

        for r in range(len(nums)):
            if minK <= nums[r] <= maxK:
                if nums[r] >= themap['max value']:
                    themap['max value'] = nums[r]
                    themap['max index'] = r
                if nums[r] <= themap['min value']:
                    themap['min value'] = nums[r]
                    themap['min index'] = r

                if themap['max value'] == maxK and themap['min value'] == minK:
                    answer += (min(themap['min index'],
                               themap['max index'])-l+1)
            else:
                l = r+1
                if l == len(nums): break
                themap = {'min index': l,
                          'min value': nums[l], 'max index': l, 'max value': nums[l]}

            # print(themap)

        return answer


# print(Solution().countSubarrays(nums=[1, 3, 5, 2, 7, 5], minK=1, maxK=5))
# print(Solution().countSubarrays(nums=[1, 3, 5, 2, 7, 5, 1], minK=1, maxK=5))

# print(Solution().countSubarrays(nums=[1, 1, 1, 1], minK=1, maxK=1))

print(Solution().countSubarrays([942922, 26282, 908345, 908345, 252308, 908345, 908345, 865114, 797201, 26282, 26282, 26282, 771220, 908345, 226478, 801741, 26282, 908345, 26282,
      628321, 26282, 26282, 26282, 317964, 908345, 375285, 212793, 389830, 26282, 26282, 908345, 199587, 225849, 137360, 908345, 26282, 881084, 938510, 991656, 920318], minK=26282, maxK=908345))
