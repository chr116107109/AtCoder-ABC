import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

N = int(input())

edge = []
g = [[0]*N for i in range(N)]
for i in range(N-1):
    A = list(map(int,input().split()))
    for j in range(N-1-i):
        edge.append([i,i+j+1,A[j]])
        g[i][i+j+1] = A[j]


d = [0] * 2**(N)

for bit in range(2**N):

    for s in range(N):
        for t in range(s+1,N):

            if bit&(1<<s) == 0 and bit&(1<<t) == 0:
                next = bit|(1<<s)|(1<<t)
                d[next] = max(d[next], d[bit] + g[s][t])

print(max(d))