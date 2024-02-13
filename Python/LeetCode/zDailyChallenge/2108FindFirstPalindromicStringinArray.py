class Solution:
    def is_palindrom(self, word: str) -> bool:
        return word == word[::-1]

    def firstPalindrome(self, words: list[str]) -> str:
        for word in words:
            if self.is_palindrom(word):
                return word
        return ''
