class Solution:
    def numberOfBeams(self, bank: list[str]) -> int:
        resArr = []
        for row in bank:
            co = row.count('1')
            if co:resArr.append(co)
        result = 0
        for i in range(1,len(resArr)):
            result+=(resArr[i]*resArr[i-1])

        print(resArr,result)

print(Solution().numberOfBeams(["011001", "000000","010100","001000"]))