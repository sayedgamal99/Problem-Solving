class Solution:
    def longestconsecutive(self,nums):
        """
        just O(n)
        
        """
        numset = set(nums)
        longest =0
        for n in numset:
            if (n-1) not in numset:
                length = 0
                while (n+length) in numset:
                    length +=1 
                longest = max(longest,length)
        return longest


class Solution2:
    def longestConsecutive(self, nums: list[int]) -> int:
        """
        O(nlog(n)) because of sorting.
        """
        nums.sort()
        ll = len(nums)
        maxx,sum=1 if ll else 0,1
        for i in range(1,len(nums)):
            if nums[i]==(nums[i-1]+1):
                sum+=1
            else:
                if nums[i]==(nums[i-1]):
                    continue
                maxx=max(sum,maxx)
                sum=1
            maxx=max(sum,maxx)

        return maxx



input = [100,1000,200,21,3,5,6,7,8,9,10,11]
# input = []
output= Solution().longestconsecutive(input)
print(output)