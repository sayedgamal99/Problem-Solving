"""

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        one = set(text1)
        two = set(text2)
        intersection = one.intersection(two)

        if len(intersection) == 0:
            return 0

        one = ''.join([letter for letter in text1 if letter in intersection])
        two = ''.join([letter for letter in text2 if letter in intersection])

        # print(one, two)

        return self.helper(one, 0, two, two)

    def helper(self, left: str, element: int, rright: str, right: str) -> int:


        if element >= len(left) or left[element] not in rright:

            return 0

        rr = right.find(left[element])
        if rr == -1:
            return 0

        a = self.helper(left, element+1, right[rr:], right)+1

        b = self.helper(left, element+2, right[rr:], right)+1

        return max(a, b)


print(Solution().longestCommonSubsequence("ezupkr", "ubmrapg"))
print('_'*30)
print(Solution().longestCommonSubsequence(text1="abcde", text2="egchda"))
print('_'*30)
print(Solution().longestCommonSubsequence(text1="abc", text2="abc"))
print('_'*30)
print(Solution().longestCommonSubsequence(text1="abc", text2="def"))
"""
