class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        def merge(A,L,M,R):
            larr,rarr = A[L:M+1],A[M+1:R+1]
            i,j,k = L,0,0
            while j < len(larr) and k < len(rarr):
                if larr[j]<=rarr[k]:
                    A[i]=larr[j]
                    j+=1
                else:
                    A[i]=rarr[k]
                    k+=1
                i+=1
            while j < len(larr):
                A[i] = larr[j]
                j +=1 
                i+=1
            while k < len(rarr):
                A[i] = rarr[k]
                k +=1 
                i+=1
            


        def merge_sort(A,l,r):
            if l == r:
                return A
            m = (l+r)//2
            merge_sort(A,l,m)
            merge_sort(A,m+1,r)
            merge(A,l,m,r)
            return A

        return merge_sort(nums,0,len(nums)-1)
        