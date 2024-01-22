n = int(input())
liss = [int(x) for x in input().split()]
from collections import Counter as CO
count_map = CO(liss)

def solve():
    if n ==1:
        return 1
    result = 0

    for ai in liss:
        stay = 0
        for j in range(32):
            ss= (1 << j)
            if ((ss-ai)>0 and ((ss-ai)in count_map and ((ss-ai != ai) or count_map[ss-ai]>1))):
                stay =1
                break

        if stay == 0:
            result+=1
    return result

print(solve())





