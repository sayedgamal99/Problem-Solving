class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        answer = []
        i=0
        while(i<min(len(word1),len(word2))):
            answer.append(word1[i])
            answer.append(word2[i])
            i+=1
        answer.extend(word1[i:])
        answer.extend(word2[i:])

        return ''.join(answer)
    
print(Solution().mergeAlternately('abc','zxkkk'))