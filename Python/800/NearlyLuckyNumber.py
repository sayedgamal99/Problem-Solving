n = (input())
rr = 0
for i in n:
    if i == '7' or i == '4':
        rr += 1
if (rr == 4 or rr ==7):
    print("YES")
else:
    print("NO")
