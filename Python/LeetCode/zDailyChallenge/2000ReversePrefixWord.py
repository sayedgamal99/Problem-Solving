class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        char_ind = word.find(ch)
        if char_ind == -1:
            return word
        return word[:char_ind+1][::-1] + word[char_ind+1:]


class SolutionLong:
    def reversePrefix(self, word: str, ch: str) -> str:
        answer = []
        new = []
        ind = 0
        for c in word:
            answer.append(c)
            if c == ch:

                while answer:
                    new.append(answer.pop())
                break
            ind += 1
        if ind == len(word):
            return word
        return ''.join(new)+word[ind+1:]


print(Solution().reversePrefix(word="abcdefd", ch="d"))
print(Solution().reversePrefix(word="abcdefd", ch="z"))
