class Solution:
    def strStr(self, haystack: str, needle: str) :
        if needle == '': return 0
        lps = [0]*len(needle)
        prevLPS,i = 0,1
        while i < len(needle):
            if needle[i] == needle[prevLPS]:
                lps[i]+= prevLPS+1
                prevLPS+=1
                i+=1
            elif prevLPS ==0:
                    lps[i]=0
                    i+=1
            else:
                prevLPS=lps[prevLPS-1]

        i,j = 0,0
        result = []
        print(lps)
        while i < len(haystack):
            print(' i:',i,' j:',j,end=' ')
            if needle[j] == haystack[i]:
                i,j=i+1,j+1
            elif j==0: i +=1
            else:
                
                
                j = lps[j-1]

            if j == len(needle):
                j=lps[j-1]
                result.append(i-len(needle))
            
        return result



        

                
T = 'SSSSHSSSHKSSSH'
P = 'SSSSH'
print(Solution().strStr(T,P))
