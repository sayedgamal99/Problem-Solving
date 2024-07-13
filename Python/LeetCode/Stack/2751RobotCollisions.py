class Solution:
    def survivedRobotsHealths(self, positions: list[int], healths: list[int], directions: str) -> list[int]:
        # Combine and sort robots by position
        robots = sorted(zip(positions, healths, directions,
                        range(len(positions))), key=lambda x: x[0])
        stack = []

        for pos, health, dir, idx in robots:
            while stack and dir == 'L' and stack[-1][2] == 'R':
                if health > stack[-1][1]:
                    health -= 1
                    stack.pop()
                elif health < stack[-1][1]:
                    stack[-1][1] -= 1
                    health = 0
                    break
                else:
                    health = 0
                    stack.pop()
                    break

            if health > 0:
                stack.append([pos, health, dir, idx])

        # Sort the stack by the original indices to get the correct order of results
        stack.sort(key=lambda x: x[3])

        return [robot[1] for robot in stack]


print(Solution().survivedRobotsHealths(
    positions=[1, 2, 5, 6], healths=[10, 10, 11, 11], directions="RLRL"))
print(Solution().survivedRobotsHealths(
    positions=[3, 5, 2, 6], healths=[10, 10, 15, 12], directions="RLRL"))
