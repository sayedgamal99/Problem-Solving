class Solution:
    def minOperations(self, nums: list[int]) -> int:
        m = max(nums)
        freq = [0]*(m+1)
        for n in nums:
            freq[n]+=1
        
        result = 0
        print(freq)
        for n in freq:
            if n%3==0: result+=(int(n/3))
            elif n==1: return -1
            else :
                result += max(int((n+1)/3), int((n+2)/3))
        
        return result


# print(Solution().minOperations([2, 3, 3, 2, 2, 4, 3, 4]))
print(Solution().minOperations(
    [14, 12, 14, 14, 12, 14, 14, 12, 12, 12, 12, 14, 14, 12, 14, 14, 14, 12, 12,
     14, 12, 14, 14, 12, 14, 14, 12, 12, 12, 12, 14, 14, 12, 14, 14, 14, 12, 12]))
