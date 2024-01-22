class Solution:
    def maxNumberOfBalloons(self, text):
        freqABC = [0]*26
        indeces= [ ord(x)-97 for x in 'balon']
        for i in text:
            if i in 'ballon':
                freqABC[ord(i)-97]+=1
        listt = [freqABC[i] for i in indeces]
        listt[2]//=2
        listt[3]//=2
        return (min(listt))
    
A = "loonbalxballpoon"
A = 'balon'
print(Solution().maxNumberOfBalloons(A))

