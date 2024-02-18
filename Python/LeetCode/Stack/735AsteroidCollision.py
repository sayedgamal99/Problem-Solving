class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        stack = []
        for a in asteroids:
            stack.append(a)
            while len(stack) > 1 and stack[-2] > 0 and stack[-1] < 0:
                if abs(stack[-1]) < abs(stack[-2]):
                    stack.pop()
                elif abs(stack[-1]) > abs(stack[-2]):
                    b = stack.pop()
                    stack.pop()
                    stack.append(b)
                else:
                    stack.pop()
                    stack.pop()

        return stack


print(Solution().asteroidCollision(asteroids=[5, -5]))
print(Solution().asteroidCollision(asteroids=[10, 5, -5, -10]))
