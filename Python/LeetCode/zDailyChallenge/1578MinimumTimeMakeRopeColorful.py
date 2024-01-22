"""
Input: colors = "aabaa", neededTime = [1,2,3,4,1]
Output: 2

"""
class Solution:
    def minCost(self, colors: str, neededTime: list[int]) -> int:
        co = None
        cost = 0
        i=1
        j=0
        while(i<len(colors)):
            # print('i',i)
            if colors[i-1]==colors[i]:
                co=colors[i-1]
                j = i-1
                while(j<len(colors)):
                    if colors[j]!=co:
                        cost+= (sum(neededTime[i-1:j])-max(neededTime[i-1:j]))
                        i=j
                        # print('j',j)
                        break
                    j+=1
                else:
                    cost += (sum(neededTime[i-1:j])-max(neededTime[i-1:j]))
                    i = j
            i +=1
            # if i==l:
            #     cost+= (sum(neededTime[i:j])-max(neededTime[i:j]))
            #     i=j
            #     print('j',j)
        return cost













colors ="aaabbb"
neededTime =[1,2,3,4,5,6]
print(Solution().minCost(colors=colors,neededTime=neededTime))
print(Solution().minCost( colors = "abaac", neededTime = [1,2,3,4,5]))
print(Solution().minCost(colors = "aabaa", neededTime = [1,2,3,4,1]))
