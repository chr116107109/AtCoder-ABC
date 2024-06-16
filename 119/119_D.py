

A,B,Q = map(int,input().split())
S = [int(input()) for i in range(A)]
T = [int(input()) for i in range(B)]
X = [int(input()) for i in range(Q)]

from bisect import bisect_left, bisect_right
S.sort()
T.sort()

for i in range(Q):
    x = X[i]
    si = bisect_left(S,x)
    ti = bisect_left(T,x)
    #print(si,ti)
    ans = 10**20
    
    if si > 0 and ti < B:
        ans = min(ans, 2*min(abs(S[si-1]-x),abs(T[ti]-x)) + max(abs(S[si-1]-x),abs(T[ti]-x)))
    if si < A and ti > 0:
        ans = min(ans, 2*min(abs(S[si]-x),abs(T[ti-1]-x)) + max(abs(S[si]-x),abs(T[ti-1]-x)))
    if si > 0 and ti > 0:
        ans = min(ans, abs(min(S[si-1],T[ti-1]) - x))
    if si < A and ti < B:
        ans = min(ans, abs(max(S[si],T[ti]) - x))


    print(ans)

