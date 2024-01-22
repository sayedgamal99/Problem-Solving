# Fibonacci solution (best):

class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1
        ans = 0
        for i in range(n-1):
            ans = one+two
            one = two
            two = ans
        return ans

# print(Solution().climbStairs(5))


# brute force

class Solution2:
    def climbStairs(self, n: int) -> int:

        def dfs(k):

            if k == n:
                return 1
            elif k > n:
                return 0
            return dfs(k+1)+dfs(k+2)

        return dfs(0)

# print(Solution2().climbStairs(5))


# memoization:

class Solution3:
    def climbStairs(self, n: int) -> int:
        cach = [-1]*(n+1)

        def dfs(k):

            if k == n:
                return 1
            elif k > n:
                return 0

            if cach[k] != -1:
                return cach[k]

            a = dfs(k+1)
            b = dfs(k+2)
            cach[k] = a + b

            return cach[k]

        result = dfs(0)
        print(cach)
        return result


print(Solution3().climbStairs(5))
