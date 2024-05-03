class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        p1 = version1.count('.')
        p2 = version2.count('.')

        if p1 < p2:
            version1 = version1+('.0'*(p2-p1))
        elif p1 > p2:
            version2 = version2+('.0'*(p1-p2))

        version1 = version1.split('.')
        version2 = version2.split('.')

        for i in range(len(version1)):
            if int(version1[i]) > int(version2[i]):
                return 1
            elif int(version1[i]) < int(version2[i]):
                return -1
        return 0
