class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        new_str = []
        for letter in s:
            if letter.isalnum(): new_str.append(letter)

        new_str = ''.join(new_str)
        right, left  = len(new_str)-1,0
        while(right>=left):
            r,l = new_str[right],new_str[left]
            if r!=l:return False
            right-=1
            left+=1
        return True
    
# print(Solution().isPalindrome('madam'))
# print(Solution().isPalindrome('A man, a plan, a canal: Panama'))
print(Solution().isPalindrome(' '))
