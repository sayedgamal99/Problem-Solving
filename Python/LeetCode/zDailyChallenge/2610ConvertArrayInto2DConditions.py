class Solution:
    def findMatrix(self, nums: list[int]) -> list[list[int]]:
        length = len(nums)+1
        freq = [0]*length
        for i in nums:
            freq[i]+=1

        n = max(freq)
        answer = []
        j=0
        while (n>0):
            n-=1
            h = []
            for i in range(1, length):
                if freq[i]:
                    freq[i]-=1
                    h.append(i)

            answer.append(h)

        return answer






print(Solution().findMatrix( [1,2,3,4]))