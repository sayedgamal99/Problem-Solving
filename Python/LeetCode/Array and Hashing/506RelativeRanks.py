from bisect import bisect_left


class Solution:
    def findRelativeRanks(self, score: list[int]) -> list[str]:
        n = len(score)
        medals = {1: 'Gold Medal', 2: 'Silver Medal', 3: 'Bronze Medal'}
        sorted_scores = score.copy()
        sorted_scores.sort()

        answer = []
        for i in range(n):
            pos = n-bisect_left(sorted_scores, score[i])
            if pos in medals:
                pos = medals[pos]
            answer.append(pos)

        return answer


print(Solution().findRelativeRanks(score=[10, 3, 8, 9, 4]))
