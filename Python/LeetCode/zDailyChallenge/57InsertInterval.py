from bisect import bisect_left, bisect, bisect_right


class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        if intervals == []:
            return [newInterval]
        l, h = newInterval[0], newInterval[1]
        all_intervals = [i for k in intervals for i in k]
        low = bisect_left(all_intervals, l)
        high = bisect_right(all_intervals, h)
        if low % 2 != 0:
            low -= 1
        if high % 2 == 0:
            high -= 1
        if high <= low:
            if newInterval[0] >= all_intervals[-1]:
                intervals.extend([newInterval])
                return intervals
            elif newInterval[1] < all_intervals[0]:
                newInterval = [newInterval]
                newInterval.extend(intervals)
                return newInterval
        new = [*all_intervals[:low], min(l, all_intervals[low]),
               max(h, all_intervals[high]), *all_intervals[high+1:]]
        new = [new[i:i+2] for i in range(0, len(new), 2)]
        return new


# print(Solution().insert([[1, 3], [6, 9]], [2, 5]))
print(Solution().insert([[1, 5]], [6, 8]))
print(Solution().insert([[1, 5]], [0, 0]))


# print(Solution().insert(intervals=[[1, 2], [3, 5], [
#       6, 7], [8, 10], [12, 16]], newInterval=[4, 8]))
