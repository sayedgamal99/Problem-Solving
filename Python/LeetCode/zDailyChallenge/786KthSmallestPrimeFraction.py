import heapq


class Solution:
    def kthSmallestPrimeFraction(self, arr: list[int], k: int) -> list[int]:
        divisions = []
        heapq.heapify(divisions)
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                heapq.heappush(divisions, (arr[i]/arr[j], [arr[i], arr[j]]))
        return heapq.nsmallest(k, divisions)[-1][1]


print(Solution().kthSmallestPrimeFraction(arr=[1, 2, 3, 5], k=3))


# another solution:


class Solution2:
    def kthSmallestPrimeFraction(self, arr: list[int], k: int) -> list[int]:
        f = []
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                f.append((arr[i], arr[j]))
        f.sort(key=lambda p: float(p[0]/p[1]))
        return f[k-1]


print(Solution2().kthSmallestPrimeFraction(arr=[1, 2, 3, 5], k=3))
