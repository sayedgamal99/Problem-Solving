from bisect import bisect_left


class Solution:
    def findClosestElements(self, arr: list[int], k: int, x: int) -> list[int]:
        nums = [0]*len(arr)
        for i in range(len(arr)):
            nums[i] = abs(arr[i]-x)
        summ = 0
        l = 0
        min_window = 0
        min_sum = float('inf')
        for r in range(len(arr)):
            if r >= k:
                if summ < min_sum:
                    min_window = l
                    min_sum = summ
                summ -= nums[l]
                l += 1
            summ += nums[r]
        if summ < min_sum:
            min_window = l
        return arr[min_window:min_window+k]


# print(Solution().findClosestElements(arr=[1, 2, 3, 4, 5], k=4, x=-1))
# print(Solution().findClosestElements(arr=[1, 2, 3, 4, 5], k=4, x=3))
# print(Solution().findClosestElements(
#     arr=[1, 2, 3, 4, 5, 10, 11, 12, 13], k=3, x=6))
# print(Solution().findClosestElements([0, 1, 2, 2, 2, 3, 6, 8, 8, 9], k=5, x=9))


# -----------------ACCEPTED-------------------

# another solution (optimization with binary search):


class Solution2:
    def findClosestElements(self, arr: list[int], k: int, x: int) -> list[int]:

        to_begin = bisect_left(arr, x)
        summ = 0
        l = to_begin-k-1 if to_begin > k else 0
        print(l, to_begin)

        min_window = 0
        min_sum = float('inf')
        r = l
        while r < len(arr) and r <= (to_begin+k-1):
            if r-l >= k:
                if summ < min_sum:
                    min_window = l
                    min_sum = summ
                summ -= abs(arr[l]-x)
                l += 1
            summ += abs(arr[r]-x)
            r += 1

        if summ < min_sum:
            min_window = l
        return arr[min_window:min_window+k]


# print(Solution2().findClosestElements(arr=[1, 2, 3, 4, 5], k=4, x=-1))
# print(Solution2().findClosestElements(arr=[1, 2, 3, 4, 5], k=4, x=3))
# print(Solution2().findClosestElements(
#     arr=[1, 2, 3, 4, 5, 10, 11, 12, 13], k=3, x=6))
# print(Solution2().findClosestElements(
#     [0, 1, 2, 2, 2, 3, 6, 8, 8, 9], k=5, x=9))

# ----------------- ACCEPTED ----------------------------


# more better solution with just binary search:


class Solution3:
    def findClosestElements(self, arr: list[int], k: int, x: int) -> list[int]:
        l, r = 0, len(arr)-k

        while l < r:
            m = (l+r)//2

            if x - arr[m] > arr[m+k] - x:
                l = m+1
            else:
                r = m
        return arr[l:l+k]
