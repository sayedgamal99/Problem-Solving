class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        stack = []
        res = [0]*len(temperatures)
        for i,temp in enumerate(temperatures):
            while stack and temp>stack[-1][-1]:
                res[stack[-1][0]] = i-stack[-1][0]
                stack.pop()
            stack.append([i,temp])
            print(stack,res)
        return res
    
print(Solution().dailyTemperatures([73,74,75,71,69,72,76,73]))
        