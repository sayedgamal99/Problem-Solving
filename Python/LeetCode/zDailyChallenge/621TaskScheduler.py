from collections import Counter


class Solution:
    def leastInterval(self, tasks, n) -> int:
        themap = Counter(tasks)
        answer = len(tasks)

        while len(themap):
            lastLength = len(themap)
            for k, v in themap.most_common(n+1):
                themap[k] -= 1
                if themap[k] == 0:
                    del themap[k]

            idle = max(0, n - lastLength + 1)
            answer += idle
        answer -= idle
        return answer


# print(Solution().leastInterval(["A", "B", "A"],2))
# print(Solution().leastInterval(['A', 'A', 'A', 'B', 'B', 'B'], 2))
# print(Solution().leastInterval(['A', 'A', 'A', 'B', 'B', 'B'], 3))
# print(Solution().leastInterval(
#     ["A", "A", "A", "B", "B", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K"], 7))
print(Solution().leastInterval(
    ["A", "A", "A", "B", "B", "B", "C", "C", "C", "D", "D", "E"], 2))
