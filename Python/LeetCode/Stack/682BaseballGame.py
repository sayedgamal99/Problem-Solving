class Solution:
    def calPoints(self, operations: list[str]) -> int:
        stack,total_sum = [],0
        for rec in operations:
            print(stack)
            try :
                ce = int(rec)
                stack.append(ce)
                total_sum+=ce
            except:
                if rec=='C':
                    total_sum-=int(stack.pop())
                elif rec=='D':
                    dd = int(stack[-1])*2
                    stack.append(dd)
                    total_sum+=int(stack[-1])
                elif rec =='+':
                    dd = int(stack[-1])+int(stack[-2])
                    stack.append(dd)
                    total_sum+=int(stack[-1])
        return total_sum,stack


# print(Solution().calPoints(["5", "-2", "4", "C", "D", "9", "+", "+"]))
print(Solution().calPoints(['1','C']))
