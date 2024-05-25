class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> list[str]:
        Answer = []
        word_set = set(wordDict)

        def backtrack(start, path):
            if start == len(s):
                Answer.append(' '.join(path))
                return

            for end in range(start+1, len(s)+1):
                word = s[start:end]
                if word in word_set:
                    backtrack(end, path+[word])

        backtrack(0, [])
        return Answer


s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
Output = ["cats and dog", "cat sand dog"]

print(Solution().wordBreak(s, wordDict))
