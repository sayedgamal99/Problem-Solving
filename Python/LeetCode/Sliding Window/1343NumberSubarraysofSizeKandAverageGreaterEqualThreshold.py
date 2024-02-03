class Solution:
    def numOfSubarrays(self, arr: list[int], k: int, threshold: int) -> int:
        avg = 0
        result = 0
        for i in range(len(arr)):
            if i >= k:
                avg -= arr[i-k]
            avg += arr[i]

            if avg/k >= threshold and i >= k-1:
                result += 1

        return result


print(Solution().numOfSubarrays(
    arr=[11, 13, 17, 23, 29, 31, 7, 5, 2, 3], k=3, threshold=5))
print(Solution().numOfSubarrays([2, 2, 2, 2, 5, 5, 5, 8], 3, 4))
