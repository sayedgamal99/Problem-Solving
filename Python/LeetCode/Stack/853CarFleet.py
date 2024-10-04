class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        stack = []
        arr = sorted(zip(position, speed), reverse=True)
        for p, s in arr:
            stack.append((target - p)/s)
            if len(stack) > 1 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)


assert Solution().carFleet(target=100, position=[
    0, 2, 4], speed=[4, 2, 1]) == 1
assert Solution().carFleet(target=12, position=[
    10, 8, 0, 5, 3], speed=[2, 4, 1, 1, 3]) == 3

print('ALL Tests Passed.')
