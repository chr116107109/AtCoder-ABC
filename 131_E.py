
import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math


N,K = map(int,input().split())

g = [[1],[]]

now = 0
ans = [[1,2]]

N -= 2
while N > 0 and K > 0:
    
    while len(g[now]) <= K:
        #print(K)
        ans.append([now+1,len(g)+1])
        K -= len(g[now])
        g[now].append(len(g))
        g.append([])
        N -= 1
    
    now += 1

if K > 0:
    print(-1)
else:
    print(len(ans))
    for a in ans:
        print(*a)