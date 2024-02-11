class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        window = 1
        l = 0
        Tracker = {}
        for r in range(len(fruits)):
            if len(Tracker) == 2 and fruits[r] not in Tracker:
                window = max(window, r-l)
                sorted_items = sorted(Tracker.items(), key=lambda x: x[1])
                print(sorted_items)
                l = sorted_items[0][1]+1
                Tracker = {sorted_items[1][0]: sorted_items[1][1]}
            Tracker[fruits[r]] = r

        return max(window, r-l+1)


print(Solution().totalFruit([0, 0, 0, 1, 2, 2, 2, 2]))
print(Solution().totalFruit([3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]))
print(Solution().totalFruit([1, 0, 1, 4, 1, 4, 1, 2, 3]))
