
import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

N,M = map(int,input().split())

S = [list(input()) for i in range(N)]

def is_ok(S):
    for i in range(N):
        for j in range(M):
            if S[i][j] == '#':
                if 0<=i+1<N and S[i+1][j] == '.':
                    return False
                if 0<=i+1<N and 0<=j+1<M and S[i+1][j+1] == '.':
                    return False
                
    return True

for i in range(N):
    for j in range(M):
        if S[i][j] == '#':
            if 0<=i+1<N and S[i+1][j] == '.':
                S[i+1][j] = '#'
            if 0<=i+1<N and 0<=j+1<M and S[i+1][j+1] == '.':
                S[i+1][j+1] = '#'
                

d = [[0] * (M+1) for i in range(N+1)]

n_dot = 0
for i in range(N-1,-1,-1):
    for j in range(M-1,-1,-1):
        d[i][j] += d[i+1][j+1]
        d[i][j] += d[i+1][j]
        if i+2 < N:
            d[i][j] -= d[i+2][j+1]
        
        if S[i][j] == '.':
            d[i][j] += 1

            n_dot += 1

ans = 1
mod=998244353
for i in range(N):
    for j in range(M):

        if S[i][j] == '.':
            ans += pow(2,n_dot-d[i][j],mod)
            ans %= mod
            n_dot -= 1
            print(ans,i,j)
print(ans)