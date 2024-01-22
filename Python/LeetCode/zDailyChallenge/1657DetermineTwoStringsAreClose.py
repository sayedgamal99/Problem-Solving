from collections import Counter as co
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        co1 = co(word1)
        co2 = co(word2)
        
        return co(co1.values())==co(co2.values()) and co1.keys()==co2.keys()



print(Solution().closeStrings(word1 = "cabbba", word2 = "abbccc"))