class Solution:
    def maxSubArray(self,nums):
        max_sum = nums[0]
        left = 0
        right = 0
        for i in range(len(nums)):
            sum = 0
            for j in range(i,len(nums)):
                sum += nums[j]
                if sum>=max_sum:
                    max_sum = sum
                    left = i
                    right = j
        return(left,right,max_sum)

problem = Solution()
A = [-2,1,-3,4,-1,2,1,-5,4]
print(problem.maxSubArray(A))
