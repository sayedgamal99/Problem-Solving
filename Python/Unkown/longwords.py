n = int(input())
while(n):
    n-=1
    word = input()
    if(len(word)>10):
        print(word[0]+f"{(len(word)-2)}"+word[-1])
    else :
        print(word)