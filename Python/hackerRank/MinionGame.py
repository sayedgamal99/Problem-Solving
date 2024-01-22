def minion_game(string):
    letters = 'AEIOU'
    n = len(string)
    winner = ()
    Kevin,Stuart = 0,0
    for ind,i in enumerate(string):
        if i in letters:
            Kevin+= n-ind
        else: Stuart += n-ind
    if Kevin>Stuart:
        return f'Kevin {Kevin}'
    elif Stuart>Kevin:
        return f'Stuart {Stuart}'
    else:
        return 'Draw'



if __name__ == '__main__':
    s = input()
    print(minion_game(s))