class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        themap = {}#letter and last index
        result = 0
        found = False
        for i in range(len(s)):
            if s[i] in themap:
                result = max(result, i-themap[s[i]]-1)
                print(result,s[i],i,themap[s[i]])
                found =True
                continue

            themap[s[i]] = i
            
        return result if found else -1

# print(Solution().maxLengthBetweenEqualCharacters("aa"))
# print(Solution().maxLengthBetweenEqualCharacters("abbcxgakkka"))
# print(Solution().maxLengthBetweenEqualCharacters('cbzxy'))
    
print(Solution().maxLengthBetweenEqualCharacters("mgntdygtxrvxjnwksqhxuxtrv"))
