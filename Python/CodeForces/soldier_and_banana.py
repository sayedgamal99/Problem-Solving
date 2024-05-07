k, n, w = list(map(int, input().split()))
res = 0
ww = k*(w*((w+1)/2))
res = n - ww
print(0 if n >= ww else int(abs(res)))
