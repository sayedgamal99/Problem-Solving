# class Solution:
#     def makeEqual(self, words: list[str]) -> bool:
#         themap = {}
        
#         sol = 0
#         lengths = 0
#         for word in words:
#             sol+=sum(ord(char)-ord('a')+1 for char in word)
#             lengths+=len(word)
#         return True if (sol%len(words)==0)and(lengths%len(words)==0) else False

    
class Solution:
    def makeEqual(self, words: list[str]) -> bool:
        themap = {}
        if len(words)==1: return True
        for word in words:
            for letter in word:
                themap[letter] = themap.get(letter,0)+1
        lengths = len(words)
        for key,val in themap.items():
            if val%lengths!=0:
                return False
        return True

        

print(Solution().makeEqual(['abc','aabc','bc']))
print(Solution().makeEqual(['ab','a']))
print(Solution().makeEqual(['bc','de']))