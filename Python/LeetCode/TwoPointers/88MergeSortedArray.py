#optimal way without extra memory:

class Solution:
    def merge(self, nums1, m, nums2, n) -> None:
        left = m
        right = n
        i = m+n-1
        while(left>0 and right>0):
            if nums1[left-1]>nums2[right-1]:
                nums1[i]=nums1[left-1]
                left -= 1
            else: 
                nums1[i] = nums2[right-1]
                right-=1
            i-=1
        while left>0:
            nums1[i] = nums1[left-1]
            i-=1
            left-=1
        while right>0:
            nums1[i] = nums2[right-1]
            i-=1
            right-=1
        return nums1



# print(Solution().merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3))
print(Solution().merge([0],0,[1],1))


#lazy way:
class Solution:
        def merge(self,nums1,m,nums2,n) ->None:
            i, j, k = 0, 0, 0
            A = [0]*(m+n)
            while j < m and k < n:
                print(A)
                if nums1[j] <= nums2[k]:
                    A[i] = nums1[j]
                    j += 1
                else:
                    A[i] = nums2[k]
                    k += 1
                i += 1
            while j < m:
                A[i] = nums1[j]
                j += 1
                i += 1
            while k < n:
                A[i] = nums2[k]
                k += 1
                i += 1

            return A
    
# print(Solution().merge([1,2,3,0,0,0], 3, [2,5,6], 3))