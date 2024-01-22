from collections import deque


class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        dom = list(dominoes)
        q = deque()
        for ind, kk in enumerate(dominoes):
            if kk != '.':
                q.append((ind, kk))
        while (q):
            i, d = q.popleft()
            if d == 'L' and i > 0 and dom[i-1] == '.':
                dom[i-1] = 'L'
                q.append((i-1, 'L'))
            elif d == 'R' and i+1 < len(dom) and dom[i+1] == '.':
                if i+2 < len(dom) and dom[i+2] == 'L':
                    q.popleft()
                else:
                    dom[i+1] = 'R'
                    q.append((i+1, 'R'))
        return ''.join(dom)


# another solution beats 99.5%
'''
class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        ss = ''
        while dominoes != ss:
            ss=dominoes
            dominoes=dominoes.replace('R.L','ccc')
            dominoes=dominoes.replace('.L','LL')
            dominoes=dominoes.replace('R.','RR')
        ss=ss.replace('ccc','R.L')
        return ss
'''


dominoes = ".L.R...LR..L.."  # INPUT
print(Solution().pushDominoes(dominoes=dominoes))
Output = "LL.RR.LLRRLL.."
