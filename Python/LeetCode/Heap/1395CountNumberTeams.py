from sortedcontainers import SortedSet


class Solution:
    def numTeams(self, rating: list[int]) -> int:
        n = len(rating)
        count = 0
        left = SortedSet([rating[0]])
        right = SortedSet(rating[2:])
        for i in range(1, n-1):
            a = left.bisect_left(rating[i])
            b = len(right) - right.bisect_right(rating[i])
            count += a*b

            a = len(left) - left.bisect_right(rating[i])
            b = right.bisect_left(rating[i])
            count += a*b

            left.add(rating[i])
            right.remove(rating[i+1])
        return count


print(Solution().numTeams([2, 5, 3, 4, 1]))  # 3
