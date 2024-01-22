class LargestNum(str):
    def __lt__(x,y):
        return x+y > y+x
class Solution:
    def largestNumber(self, nums: list[int]) -> str:
        nums = [str(num) for num in nums]
        nums.sort(key=LargestNum)
        result = ''.join(nums)
        return result if result[0]!='0' else 0
    


numss = [3,34,30,9,5]
print(Solution().largestNumber(numss))
