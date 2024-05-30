class Solution:
    def countTriplets(self, arr: list[int]) -> int:
        n = len(arr)
        answer = 0
        for i in range(n):
            xor = 0
            for j in range(i, n):
                xor = xor ^ arr[j]
                if xor == 0:
                    answer += (j-i)
        return answer
