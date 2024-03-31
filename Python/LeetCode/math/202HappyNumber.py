# brute force (accepted).
class Solution:
    def summ(self, n):
        total_sum = 0
        while n > 0:
            digit = n % 10
            total_sum += (digit**2)
            n //= 10
        return total_sum

    def isHappy(self, n: int) -> bool:
        numbers = set()
        while n not in numbers and n != 1:
            numbers.add(n)
            n = self.summ(n)
        return n == 1


print(Solution().isHappy(5))


# another solution (dummy :))

class Solution:
    def isHappy(self, n: int) -> bool:
        strn = str(n)
        j = 0
        sum = 0
        numbers = []
        while sum != 1 and j < 100:
            j += 1
            sum = 0
            for i in strn:
                sum += (int(i)**2)
            strn = str(sum)
            if sum != 1:
                numbers.append(sum)
            # print(numbers)
        else:
            return True if j < 15 else False
