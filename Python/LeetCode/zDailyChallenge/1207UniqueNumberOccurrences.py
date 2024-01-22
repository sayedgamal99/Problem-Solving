class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        themap = {}
        for element in arr:
            themap[element] = themap.get(element,0)+1
        return len(themap.values())==len(set(themap.values()))
    
print(Solution().uniqueOccurrences([1, 2,2,1,1,3]))