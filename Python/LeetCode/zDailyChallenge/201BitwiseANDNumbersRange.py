class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        left = format(left, 'b').zfill(right.bit_length())
        right = bin(right)[2:]
        result = [0]*len(left)

        label = False
        for j in range(len(left)):
            if left[j] != right[j]:
                label = True
            if label:
                result[j] = '0'
            else:
                result[j] = right[j]

        return int(''.join(result), 2)


print(Solution().rangeBitwiseAnd(5, 7))
print(Solution().rangeBitwiseAnd(5, 5))

print(Solution().rangeBitwiseAnd(0, 0))
print(Solution().rangeBitwiseAnd(left=1, right=2147483647))
