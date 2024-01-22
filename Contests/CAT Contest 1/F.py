i = int(input())
strr = input()

freq = [0]*26
for j in strr:
    freq[ord(j)-97]+=1
res = ''
key = True

for ll in freq:
    if ll !=0 and ll%i!=0:
        key = False

while(max(freq)!=0 and key):
    # print(max(freq))
    for ind,jj in enumerate(freq):
            if jj>0:
                kk = (chr(ind+97))*(jj//i)
                freq[ind]-=(jj//i)
                res +=kk
                # print(res)
    i-=1
    


# print(res)
print(res if len(res)==len(strr) else -1)
