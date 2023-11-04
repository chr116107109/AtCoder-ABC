import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools


X,Y,Z = map(int,input().split())

S = input()
N = len(S)

A = []

now = ''
for i in range(N):
    if S[i] == now:
        A[-1][1] += 1
    else:
        A.append([S[i],1])
        now = S[i]

ans = 0
d = [[0,10**20] for i in range(len(A)+1)]
for i in range(1,len(A)+1):
    s,count = A[i-1]
    
    if s == 'a':
        d[i][0] = min(d[i-1][0]+count*X, d[i-1][1]+Z+count*X)
        d[i][1] = min(d[i-1][1]+count*Y, d[i-1][0]+Z+count*Y)
    if s == 'A':
        d[i][1] = min(d[i-1][1]+count*X, d[i-1][0]+Z+count*X)
        d[i][0] = min(d[i-1][0]+count*Y, d[i-1][1]+Z+count*Y)

print(min(d[-1]))
