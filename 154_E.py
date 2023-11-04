

N = int(input())
K = int(input())
M = len(str(N))
ans = 0
import math
for i in range(K,M):
    ans += pow(9,K)*math.comb(i-1,K-1)

import itertools
#print(ans)

head = N//pow(10,M-1)
ans += (head-1)*math.comb(M-1,K-1)*pow(9,K-1)
if K == 1:
    ans += 1 # head分の加算
    print(ans)
elif K == 3:
    head *= pow(10,M-1)
    for i,j in itertools.combinations(range(M),2):
        for s,t in itertools.product(range(1,10),range(1,10)):
            if N >= head + s*pow(10,i) + t*pow(10,j):
                ans += 1
    print(ans)
elif K == 2:
    head *= pow(10,M-1)
    for i in range(M):
        for s in range(1,10):
            if N >= head + s*pow(10,i):
                ans += 1
    print(ans)