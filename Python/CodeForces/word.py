word = input().strip()
up = 0;low = 0
# print(ord(word[2]))
# print(chr(33))
for i in word:
    if ord(i)>=97:
        low+=1
    else:
        up+=1
if low>=up:
    print(word.lower())
else:
    print(word.upper())



