from collections import Counter


class Solution:
    def maxScoreWords(self, words: list[str], letters: list[str], score: list[int]) -> int:

        themap = Counter(letters)

        def dfs(i, count, s):
            if i == len(words):
                return s  # score
            # option 1: skip current word
            max_score = dfs(i+1, count, s)

            # option 2: use the current word (if possible)

            word = words[i]
            word_score = 0
            can_use = True

            temp_count = count.copy()
            for char in word:
                if temp_count[char] <= 0:
                    can_use = False
                    break
                temp_count[char] -= 1
                word_score += score[ord(char) - ord('a')]

            if can_use:
                max_score = max(max_score, dfs(i+1, temp_count, s+word_score))

            return max_score
        return dfs(0, themap, 0)


words = ["leetcode"]
letters = ["l", "e", "t", "c", "o", "d"]
score = [0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1,
         0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]

solution = Solution()
print(solution.maxScoreWords(words, letters, score))  # Expected output: 0
