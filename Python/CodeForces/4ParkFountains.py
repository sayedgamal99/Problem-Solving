from bisect import bisect_right, bisect_left


def solution(n, q, A, Q):
    Q.sort()
    answer = 0
    for i, a in enumerate(A):
        bi = bisect_right(Q, i)
        num = q-bi
        if num >= a:
            answer += 1

    return answer


n, q = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]
Q = [int(input()) for _ in range(q)]


print(solution(n, q, A, Q))
