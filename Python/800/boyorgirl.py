inpuut = input()
filtt = ''
for i in range(len(inpuut)):
    if inpuut[i] in filtt:
        continue
    else:
        filtt+=inpuut[i]
if(len(filtt)%2 ==0 ):
    print('CHAT WITH HER!')
else:
    print('IGNORE HIM!')


    