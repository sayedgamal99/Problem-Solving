class Solution:
    def zeroFilledSubarray(self, nums: list[int]) -> int:
        zeros,result=0,0
        def calc_them(n_zeros):
            return n_zeros*(n_zeros+1)//2
        for z in nums:
            if z==0:
                zeros+=1
            else:
                result+=calc_them(zeros)
                zeros=0
        result+=calc_them(zeros)
        return result


                