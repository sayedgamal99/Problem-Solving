# Two pointer Solution:
class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        l,r = 0,len(numbers)-1
        while(l<r):
            summ = numbers[l]+numbers[r]
            if summ>target:
                r-=1
            elif summ<target:
                l+=1
            else:
                return [l+1,r+1]
            

print(Solution().twoSum([2, 7, 11, 15], 9))

# Binary Search Solution:
from bisect import bisect_left
class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:

        for i in range(len(numbers)):
            required = target-numbers[i]
            idx = bisect_left(numbers, required)
            print(idx)
            if (idx<len(numbers))and numbers[idx] == required and i!=idx :
                return sorted([i+1, idx+1])


# print(Solution().twoSum([2, 7, 11, 15], 9))
# print(Solution().twoSum([5,25,75],100))

# using map Solution:


class Solution2:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        themap = {num: idx for idx, num in enumerate(numbers)}
        numbers = [target-n for n in numbers]
        for i in range(len(numbers)):
            # print(numbers[i],themap,i)
            if numbers[i] in themap:
                return sorted([i+1, themap[numbers[i]]+1])


# print(Solution2().twoSum([2, 7, 11, 15], 9))
