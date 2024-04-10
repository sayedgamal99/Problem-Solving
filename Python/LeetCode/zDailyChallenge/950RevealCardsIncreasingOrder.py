from collections import deque


class Solution:
    def deckRevealedIncreasing(self, deck: list[int]) -> list[int]:

        deck.sort()

        n = len(deck)
        result = [0] * n
        indices = deque(range(n))

        for card in deck:
            result[indices.popleft()] = card
            if indices:
                indices.append(indices.popleft())

        return result


print(Solution().deckRevealedIncreasing(deck=[17, 13, 11, 2, 3, 5, 7]))
