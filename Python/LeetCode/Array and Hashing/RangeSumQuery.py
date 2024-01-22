class NumArray:

    def __init__(self, nums):
        self.nums = nums
        self.comArray,self.summ = [],0
        for i in self.nums:
            self.summ+=i
            self.comArray.append(self.summ)
        print(self.comArray)

    def sumRange(self, left: int, right: int) -> int:
        if left ==0:
            return self.comArray[right]

        return self.comArray[right]-self.comArray[left-1]

A =NumArray([-2, 0, 3, -5, 2, -1])
print(A.sumRange(0,2))
print(A.sumRange(0,5))
print(A.sumRange(2,5))

"""
-2, 0, 3, -5, 2, -1

comarray =
-2 -2 1 -4 -2 -3

"""