n = int(input())
segments = list(map(int, input().split()))

segments.sort()

for i in range(n - 2):
    if segments[i] + segments[i + 1] > segments[i + 2]:
        print("YES")
        break
else:
    print("NO")