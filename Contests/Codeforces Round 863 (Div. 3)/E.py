def funn(k):
    digit = []
    while(k>0):
        digit.append(k%9)
        k//=9
    digit.reverse()
    return ''.join(str(d) if d < 4 else str(d + 1) for d in digit)



num_tests = int(input())

for t in range(num_tests):
    k = int(input())
    result = funn(k)
    print(result)