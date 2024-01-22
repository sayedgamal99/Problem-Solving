S = input()
open, close = '(<{[', ')}>]'

def findlongest(S):
    freqq = [0]*1000001
    stt = []
    longest, long,op = 0, 0,[]
    for i in S:
        if len(stt) != 0 and (ord(stt[-1]) == (ord(i)-2) or ord(stt[-1]) == (ord(i)-1)):
            stt.pop()
            long += 2
            if len(op) and op[-1]==0:
                op.pop()
                if long:
                    op.append(long)

        elif i in open:
            stt.append(i)
            op.append(0)
        else:
            # op.append(long)
            longest = max(longest, long)
            freqq[long] += 1 if long else 0 
            long = 0
            stt.append(i)

    longest = max(longest, long)
    freqq[long] += 1 if long else 0
    print(op)
    
    return longest, freqq[longest] if longest else 1

print(*findlongest(S))
