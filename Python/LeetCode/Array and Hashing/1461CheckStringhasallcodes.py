class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        sett= set()
        n = len(s)
        for i in range(k,n+1):
            sett.add(s[i-k:i])
            if len(sett)==1<<k:
                return True
        return False 
    

# V-1.2
"""
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        got = {s[i - k : i] for i in range(k, len(s) + 1)}
        return len(got) == 1 << k
"""
# V-1.0 
"""
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        sett= set()
        for i in range(1>>k):
            sett.add(format(i,f'0{k}b'))
        n = len(s)
        # print(sett)
        for i in range(k,n+1):
            if s[i-k:i] in sett:
                sett.remove(s[i-k:i])
        return False if sett else True
    
"""

s,k = "0110",2
print(Solution().hasAllCodes(s,k))

