t= int(input().strip())
while(t>0):
    
    n = int(input().strip())
    stri = list(input().strip())
    while(len(stri)>0):
        if ((stri[0]== '0' and stri[-1]=='1')or((stri[0]== '1' and stri[-1]=='0'))):
            stri.pop(0)
            stri.pop(-1)
            # print('pooped')
        else:
            # print('wha')
            break
    print(len(stri))
    t-=1




