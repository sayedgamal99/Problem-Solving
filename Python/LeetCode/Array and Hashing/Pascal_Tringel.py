"""
# brute force solution:

n = int(input().strip())
liss = [[1]]
for i in range(n):
    liss.append([])
    for ii in range(i+1):
        if ii == 0 :
            liss[i+1].append(liss[i][ii])
        elif ii == i:
            liss[i+1].append(liss[i][ii-1])
        else:
            liss[i+1].append(liss[i][ii]+liss[i][ii-1])

            


liss.pop(0)
print(liss)

"""

# math solution with combinations:
import math
class Solution:
    def pascalTringle(self,n):
        def factorial(n):
            return math.factorial(n)

        def combinaitons(n,k):
            res = (factorial(n)//(factorial(k)*factorial(n-k)))
            return res

        fin_res = []
        for i in range(n):
            res =[]
            for k in range(0,i+1):
                res.append(combinaitons(i,k))
            fin_res.append(res)
        return fin_res


        
print(Solution().pascalTringle(5))