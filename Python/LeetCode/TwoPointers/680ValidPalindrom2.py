from collections import Counter as CO
class Solution:
    def __init__(self):
        self.valid = 0
    def validPalindrome(self, s: str) -> bool:
        length = len(s)
        if length==1:return True

        left,right = 0,length-1
        while (left<=right):
            if s[left]==s[right]:
                left+=1
                right-=1
            else:
                if self.valid>0:return False
                self.valid += 1
                a= self.validPalindrome(s[left:right])
                print('hey',a)
                b= self.validPalindrome(s[left+1:right+1])
                print('hi',b)

                return a or b

        return True
        # return a or b

        

# print(Solution().validPalindrome('abca'))
# print(Solution().validPalindrome('abcca'))

# print(Solution().validPalindrome('cbbcc'))
# print(Solution().validPalindrome('eccer'))

# print(Solution().validPalindrome(
#     'aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga'))


class Solution2:
    def validPalindrome(self, s: str) -> bool:
        co = CO(s)

        length = len(s)
        if length == 1:
            return True

        left, right = 0, length-1
        valid = 0
        while (left <= right):
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:

                if valid > 0:
                    return False
                if co[s[left]] % 2 != 0:
                    left += 1
                else:
                    right -= 1

                valid += 1
        return True

print(Solution2().validPalindrome('eccer'))

print(Solution2().validPalindrome(
    'aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga'))

print(Solution2().validPalindrome('aaaz'))

print(Solution2().validPalindrome('zazazr'))
