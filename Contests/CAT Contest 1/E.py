n = int(input())
liss = [int(x) for x in input().split()]

fin_seq = 1
seq=1
for i in range(1,n):
    if liss[i]>liss[i-1]:
        seq+=1
    else:
        fin_seq=max(seq,fin_seq)
        seq=1

fin_seq=max(seq,fin_seq)

    
print(fin_seq)

