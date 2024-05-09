class Solution:
    def maximumHappinessSum(self, happiness: list[int], k: int) -> int:
        happiness.sort()
        r = len(happiness)-1
        decrements = 0
        answer = 0
        while k:
            answer += (happiness[r]-decrements)
            r -= 1
            k -= 1
            decrements += 1

        return answer
