from collections import Counter


class Solution:
    def relativeSortArray(self, arr1: list[int], arr2: list[int]) -> list[int]:
        freqA = Counter(arr1)
        answer = []
        for i in range(len(arr2)):
            answer.extend([arr2[i]]*freqA[arr2[i]])
            del freqA[arr2[i]]
        sortedKeys = sorted(freqA)
        for k in sortedKeys:
            answer.extend([k]*freqA[k])
        return answer


print(Solution().relativeSortArray(
    arr1=[2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19], arr2=[2, 1, 4, 3, 9, 6]))
