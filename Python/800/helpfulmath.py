the = map(int,input().split('+'))
thelist = list(the)
thelist.sort()
for num in range(len(thelist)):
    if num == (len(thelist)-1):
        print(thelist[num],end='')
        break
    print(thelist[num],end='+')



