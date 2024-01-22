class Solution:
    def findDisappearedNumbers(self, nums):
        n = len(nums)
        freq = [0]*(n+1)
        for i in nums:
            freq[i]+=1
        A=[]
        for i in range(1,n+1):
            if freq[i] == 0:
                A.append(i) 
        return A
        
# A = [1,1]
A = [4,3,2,7,8,2,3,1]
instance = Solution()
print(instance.findDisappearedNumbers(A))