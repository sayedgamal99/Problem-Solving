t = int(input())
i = 0
conv = {'a':'V','e':'V','c':'C','d':'C','b':'C'}
while(i<t):
    i+=1
    n = int(input())
    word = input()
    wordconv = [conv[j] for j in word]
    # print(word,wordconv)
    ccs = set()
    for kk in range(1,n):
        if (wordconv[kk-1]=='C' and wordconv[kk]=='C')or (n-1>kk>1 and wordconv[kk]=='C' and wordconv[kk-1]=='V' and wordconv[kk+1]=='V'):
            ccs.add(kk)
    # print(ccs)
    new_word = []
    for m in range(n):
        if m in ccs:
            new_word.append('.')
        new_word.append(word[m])
    print(''.join(new_word))