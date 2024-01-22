n = input()
word = input()

letters = [0]*26
for i in word:
    letters[ord(i)-97]+=1

res = 0
num = 0
for i in letters:
    if i:
        num+=1
    if i >1:
        res +=i-1
print(res) if (26 - num >= res) else print(-1)