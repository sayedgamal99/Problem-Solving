class Solution:
    def averageWaitingTime(self, customers: list[list[int]]) -> float:
        current_time = 0
        waiting = 0
        for arrival, time in customers:
            if arrival < current_time:
                waiting += abs(arrival-current_time)
            else:
                current_time = arrival

            waiting += time
            current_time += time

        return waiting/float(len(customers))


print(Solution().averageWaitingTime(customers=[[1, 2], [2, 5], [4, 3]]))
print(Solution().averageWaitingTime(
    customers=[[5, 2], [5, 4], [10, 3], [20, 1]]))
print(Solution().averageWaitingTime(
    [[2, 3], [6, 3], [7, 5], [11, 3], [15, 2], [18, 1]]))
