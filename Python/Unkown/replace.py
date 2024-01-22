S =input().strip()
letters = [0]*26
for letter in S:
    letters[ord(letter)-97]+=1
for ind,count in enumerate(letters):
    if count:
        print(f'{chr(ind+97)} : {count}')
