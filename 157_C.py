
import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

N,M = map(int,input().split())

visited = {}
for i in range(M):
    s,c = map(int,input().split())
    if (s in visited and visited[s] != c):
        print(-1)
        sys.exit()
    visited[s] = c

for i in range(10**N):
    t = str(i)
    if len(t) !=  N:
        continue
    ok = True
    #print(t)
    for s in visited:
        if t[s-1] != str(visited[s]):
            ok = False

    if ok:
        print(i)
        sys.exit()

print(-1)