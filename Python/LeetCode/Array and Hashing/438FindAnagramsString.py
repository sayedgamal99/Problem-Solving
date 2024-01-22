from collections import Counter 
class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        def compare_maps(map1, map2):
            letter_counts = [0] * 26
            for letter,val in map1.items():

                index = ord(letter) - 97
                # print(index)
                letter_counts[index] += val
            for letter,val in map2.items():
                index = ord(letter) - 97
                letter_counts[index] -= val
            for count in letter_counts:
                if count != 0:
                    return False
            return True
        
        if len(p)> len(s):return []
        sCount,pCount = Counter(s[:len(p)]),Counter(p)

        res = [0] if compare_maps(sCount,pCount) else []

        l = 0
        for r in range(len(p),len(s)):
            sCount[s[r]] = 1 + sCount.get(s[r],0)
            sCount[s[l]]-=1

            if sCount[s[l]] ==0:
                sCount.pop(s[l])
            
            l+=1
            if compare_maps(sCount,pCount):
                res.append(l)

        return res







print(Solution().findAnagrams('abcsdflcabkjcba','abc'))
print(Solution().findAnagrams('abab','ab'))
print(Solution().findAnagrams('abab','aab'))


