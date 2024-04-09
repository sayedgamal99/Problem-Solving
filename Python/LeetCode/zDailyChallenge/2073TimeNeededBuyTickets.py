from collections import deque

# --------------- one pass solution ----------------


class Solution:
    def timeRequiredToBuy(self, tickets: list[int], k: int) -> int:
        return sum(min(x, tickets[k] if i <= k else tickets[k]-1)for i, x in enumerate(tickets))


print(Solution().timeRequiredToBuy(tickets=[2, 3, 2], k=2))
print(Solution().timeRequiredToBuy(tickets=[5, 1, 1, 1], k=0))
print(Solution().timeRequiredToBuy(tickets=[2,2,4,2], k=2))


# --------------- simple brute force solution ------------------


class Solution2:
    def timeRequiredToBuy(self, tickets: list[int], k: int) -> int:
        sec = 0
        i = 0
        while tickets[k]:
            if tickets[i]:
                tickets[i] -= 1
                sec += 1
            i = (i+1) % len(tickets)
        return sec


# --------------- Using Queue Solution (as explanation needed) ----------------


class Solution3:
    def timeRequiredToBuy(self, tickets: list[int], k: int) -> int:
        tickets = deque(tickets)
        seconds = 0
        i = 0
        while tickets[k]:
            tickets[i] -= 1
            seconds += 1
            if tickets[i]:
                tickets.append(tickets.popleft())
                k = k-1 if k != i else (len(tickets)-1)
            else:
                tickets.popleft()
                if k != i:
                    k -= 1
                else:
                    return seconds

        return seconds
