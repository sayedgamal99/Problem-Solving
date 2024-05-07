n = int(input())
maxx = 0
ai = 0
bi = 0
inn= 0
for _ in range(n):
    ai,bi  = list(map(int,input().split()))
    inn = inn + (bi-ai)
    maxx = max(maxx,inn)
print(maxx)
