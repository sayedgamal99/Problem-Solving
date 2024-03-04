class Solution:
    def bagOfTokensScore(self, tokens: list[int], power: int) -> int:
        tokens.sort()
        n = len(tokens)

        l, r = 0, n-1
        score = 0
        while l <= r:
            if tokens[l] <= power:
                score += 1
                power -= tokens[l]
                l += 1
            elif score and r-l > 1:
                score -= 1
                power += tokens[r]
                r -= 1
            else:
                break
        return score


print(Solution().bagOfTokensScore(tokens=[100, 200, 300, 400], power=200))
