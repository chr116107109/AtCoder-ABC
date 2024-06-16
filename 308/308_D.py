import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

H,W = map(int,input().split())
S = [input() for i in range(H)]

q = deque()
q.append([(0,0),S[0][0]])
visited = {}
A = list('snuke')
while q:
    s,now = q.popleft()
    if s in visited or not now in A:
        continue
    visited[s] = now

    for t in [(s[0]+1,s[1]),(s[0],s[1]+1),(s[0]-1,s[1]),(s[0],s[1]-1)]:
        if 0<=t[0]<H and 0<=t[1]<W and S[t[0]][t[1]] in A and (A.index(now)+1)%5 == A.index(S[t[0]][t[1]]):
            q.append([t,S[t[0]][t[1]]])

if (H-1,W-1) in visited:
    print('Yes')
else:
    print('No')