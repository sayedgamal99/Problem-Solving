from collections import Counter
class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        mapp = Counter(people)

        people = [limit - p for p in people]
        
        boats = 0

        for j in people:
            if j not in mapp:
                boats+=1
            else:
                if mapp[j]<mapp[limit-j]:
                    





                # boats+= min(mapp[j],mapp[limit-j])

                
                

        return boats



print(Solution().numRescueBoats(people = [3,5,3,1,4], limit = 5))