class Solution:
    def topKFrequent(self, nums, k) :
        dict = {}
        for key in (nums):
            dict[key]=dict.get(key,0)+1
        return sorted(dict,key=dict.get,reverse=True)[:k]
    
nums = [1,1,1,2,2,3,-1]
k=2
print(Solution().topKFrequent(nums,k))
