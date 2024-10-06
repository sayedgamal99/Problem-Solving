class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        i, j = 0, 0
        sentence1 = sentence1.split()
        sentence2 = sentence2.split()

        if len(sentence1) > len(sentence2):
            sentence1, sentence2 = sentence2, sentence1

        while i < len(sentence1) and sentence1[i] == sentence2[j]:
            i += 1
            j += 1

        i_back, j_back = len(sentence1) - 1, len(sentence2) - 1
        while i_back >= 0 and sentence1[i_back] == sentence2[j_back]:
            i_back -= 1
            j_back -= 1

        return i_back < i


assert Solution().areSentencesSimilar(
    sentence1="My name is Haley", sentence2="My Haley") == True

assert Solution().areSentencesSimilar(
    sentence1="lot", sentence2="A lot of words") == False

print('All tests passed')
