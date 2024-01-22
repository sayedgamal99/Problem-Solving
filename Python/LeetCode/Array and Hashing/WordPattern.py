class Solution:
    def wordPattern(self, pattern, s):
        dict = {}
        if len(pattern)!=len(s.split()) or (len(set(pattern))!=len(set(s.split()))):
            return False
        for pat,ss in zip(pattern,s.split()):
            if pat not in dict:
                dict[pat] = ss
            else:
                if dict[pat] != ss:
                    return False

        return True

print(Solution().wordPattern('abba','dog dog dog dog'))