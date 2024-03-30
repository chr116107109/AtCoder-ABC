import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math


T = input()
N = int(input())

S = []

for i in range(N):
    s = input().split()
    S.append(s[1:])


inf = 10**9
d = [[inf] * (len(T)+1) for _ in range(N+1)]

d[0][0] = 0

for i in range(N):
    for j in range(len(T)+1):
        
        d[i+1][j] = min(d[i+1][j],d[i][j])
        for k in range(len(S[i])):
            kouho =  T[:j] + S[i][k]

            if len(kouho) > len(T):
                continue
            
            if kouho == T[:len(kouho)]:
                d[i+1][len(kouho)] = min(d[i+1][len(kouho)],d[i][j]+1)


if d[N][len(T)] != inf:
    print(d[N][len(T)])
else:
    print(-1)

