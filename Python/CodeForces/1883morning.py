n = int(input())
for i in range(n):
    pin = list(map(int,input().strip()))
    pin = [i if i != 0 else 10 for i in pin]
    result = 4+abs(1-pin[0])+abs(pin[0]-pin[1])+abs(pin[1]-pin[2])+abs(pin[2]-pin[3])
    print(result)

