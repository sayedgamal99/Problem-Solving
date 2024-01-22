class Solution:
    def alphabetical_order(self,s):
        maxi,result = 0,''
        for i in s:
            if ord(i)>=maxi:
                maxi=ord(i)
                result+=i
        return result
    
print(Solution().alphabetical_order('abdulrahman'))
print(Solution().alphabetical_order('AAAABBBCCCZZZAAA'))
