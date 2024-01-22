import math
import os
import random
import re
import sys

def diagonalDifference(arr):
    right_diagnola,left_diagonal = 0,0
    for i in range(len(arr)):
        right_diagnola+=arr[i][i]
        left_diagonal +=arr[i][len(arr)-1-i]
        
    return abs(right_diagnola-left_diagonal)

if __name__ == '__main__':


    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
