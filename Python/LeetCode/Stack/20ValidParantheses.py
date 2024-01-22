class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        for br in s:
            if br in '[({':
                stack.append(br)
            else: 
                if stack:
                    closed  = stack.pop(-1)
                    if not abs(ord(closed)-ord(br))<3: return False
                else: return False
        return False if stack else True
    
# print(Solution().isValid('{([])}'))
# print(Solution().isValid('{}()[]'))
print(Solution().isValid('['))
