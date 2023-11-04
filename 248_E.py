

import itertools
import math

N,K = map(int,input().split())
A = [list(map(int,input().split())) for i in range(N)]
C = set()
C_n = []
if K == 1:
    print('Infinity')
else:
    ans = 0
    for i,j in itertools.combinations(range(N),2):
        a = A[j][0] - A[i][0]
        b = A[j][1] - A[i][1]
        c = A[i][1]*a - A[i][0]*b
        flag = True
        n_on = 0
        g = math.gcd(a,b)
        g = math.gcd(g,c)
        a //= g
        b //= g
        c //= g
        if a < 0 or (a==0 and b < 0) or (a==0 and b==0 and c < 0):
            a,b,c = -a,-b,-c
        if (a,b,c) in C:
            continue
        C.add((a,b,c))
        for k in range(N):
            if A[k][1]*a == A[k][0]*b + c:
                n_on += 1
        if n_on >= K:
            ans += 1
        #print(A[i],A[j],n_on)
        
    print(ans)