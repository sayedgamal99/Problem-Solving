class Solution:
    def minimumDifference(self, nums: list[int], k: int) -> int:
        length = len(nums)
        if length==1:return 0
        nums.sort()
        left=0;right=left+k-1;mini=99999999
        for i in range(length):
            mini=min(mini,abs(nums[left]-nums[right]))
            left+=1;right+=1
            if right==length:break
        
        return mini

print(Solution().minimumDifference([9,4,1,7],2))