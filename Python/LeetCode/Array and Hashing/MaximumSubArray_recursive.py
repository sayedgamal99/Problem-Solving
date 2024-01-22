

class Solution:
    def Find_maxSubArray(self,low,high,A):
        if high == low+1:
            return (low,low,A[low])
        else:
            mid = (low+high)//2

        leftlow,lefthigh,leftsum=self.Find_maxSubArray(low,mid,A)
        rightlow,righthigh,rightsum=self.Find_maxSubArray(mid,high,A)
        crosslow,crosshigh,crosssum=self.Find_crossing_maxSum(low,mid,high,A)
        if leftsum>= rightsum and leftsum>=crosssum:
            return (leftlow,lefthigh,leftsum)
        elif rightsum>= leftsum and rightsum>=crosssum:
            return (rightlow,righthigh,rightsum)
        else:
            return (crosslow,crosshigh,crosssum)

    
    def Find_crossing_maxSum(self,low,mid,high,A):
        leftsum = -999999
        maxleft,maxright=0,len(A)-1
        summ = 0
        for i in reversed(range(low,mid)):
            summ +=A[i]
            if summ>leftsum:
                leftsum=summ
                maxleft=i
        rightsum = -9999999
        summ = 0
        for j in range(mid,high):
            summ+=A[j]
            if summ>rightsum:
                rightsum=summ
                maxright=j
        return(maxleft,maxright,(leftsum+rightsum))
        
    def maxSubArray(self, nums) -> int:
        return((self.Find_maxSubArray(0,len(nums),nums)[2]))
    