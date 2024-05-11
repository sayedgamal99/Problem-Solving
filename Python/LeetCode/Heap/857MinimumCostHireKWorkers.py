import heapq

# TLE


class Solution:
    def mincostToHireWorkers(self, quality: list[int], wage: list[int], k: int) -> float:
        n = len(wage)

        heap = []
        heapq.heapify(heap)

        thesum = []
        heapq.heapify(thesum)

        for i in range(n):
            thesum.clear()
            wag_qua = wage[i]/quality[i]
            for j in range(n):
                w = wag_qua*quality[j]
                if w >= wage[j]:
                    heapq.heappush(thesum, w)
            if len(thesum) >= k:
                res = sum(heapq.nsmallest(k, thesum))
                heapq.heappush(heap, res)

        return heap[0]


print(Solution().mincostToHireWorkers(
    quality=[10, 20, 5], wage=[70, 50, 30], k=2))


# editorial solution:


class Solution:
    def mincostToHireWorkers(self, quality: list[int], wage: list[int], k: int) -> float:
        n = len(quality)
        total_cost = float("inf")
        current_total_quality = 0
        wage_to_quality_ratio = []

        # Calculate wage-to-quality ratio for each worker
        for i in range(n):
            wage_to_quality_ratio.append((wage[i] / quality[i], quality[i]))

        # Sort workers based on their wage-to-quality ratio
        wage_to_quality_ratio.sort(key=lambda x: x[0])

        # Use a heap to keep track of the highest quality workers
        highest_quality_workers = []

        # Iterate through workers
        for i in range(n):
            heapq.heappush(highest_quality_workers, -
                           wage_to_quality_ratio[i][1])
            current_total_quality += wage_to_quality_ratio[i][1]

            # If we have more than k workers,
            # remove the one with the highest quality
            if len(highest_quality_workers) > k:
                current_total_quality += heapq.heappop(highest_quality_workers)

            # If we have exactly k workers,
            # calculate the total cost and update if it's the minimum
            if len(highest_quality_workers) == k:
                total_cost = min(
                    total_cost, current_total_quality *
                    wage_to_quality_ratio[i][0]
                )

        return total_cost
