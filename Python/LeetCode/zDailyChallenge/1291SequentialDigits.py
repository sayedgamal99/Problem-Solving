import time



class Solution:
    def sequentialDigits(self, low: int, high: int) -> list[int]:
        low = str(low)
        high = str(high)
        result = []
        i = 0

        lenn = len(low)
        limit = 10 - lenn
        while True:
            number = [int(low[0])+i]
            for j in range(1, len(low)):
                temp = number[-1]+1
                number.append(temp)

            print(number)
            number = ''.join(list(map(str, number)))
            print(number)
            if int(number[0]) >= limit+1 and limit:
                limit -= 1
                low = '1'+('0'*len(low))
                i=0
                print(low,'low')
                print(limit,'limit')

                continue
            if limit ==0:break
            if int(high) >= int(number):
                if int(number)>=int(low):
                    result.append(int(number))
            else:
                break
            i += 1
        return result


# print(Solution().sequentialDigits(low=1000, high=13000))
# print(Solution().sequentialDigits(low = 58,high=155))
# print(Solution().sequentialDigits(low=8511, high=23553))
print(Solution().sequentialDigits(low=10, high=1000000000))
