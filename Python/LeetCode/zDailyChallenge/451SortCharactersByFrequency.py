from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        freq = Counter(s)
        sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
        answer = []
        for k, v in sorted_freq:
            answer.append(k*v)
        return ''.join(answer)


print(Solution().frequencySort('treehhh'))
