

import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

N = int(input())
P = list(map(int,input().split()))
Q = list(map(int,input().split()))

g = [[] for i in range(N)]
for i in range(N):
    a,b = P[i], Q[i]
    g[a-1].append(b-1)
    g[b-1].append(a-1)


ans = 1

from collections import deque
def bfs(s):
    q = deque()
    q.append((s,0))
    visited = {}
    while q:
        s,d = q.popleft()
        if s in visited:
            continue
        visited[s] = d
        for t in g[s]:
            q.append((t,d+1))
    return visited

visited = {}
mod=998244353
for i in range(N):
    if not i in visited:
        v = bfs(i)
        
        a = 1
        b = 1
        for j in range(len(v)-1):
            #print(a,b)
            a,b = a+b,a
        
        ans *= (a+a-b)
        ans %= mod
        visited.update(v)
print(ans)

def greedy():
    ans = 0
    for bit in range(2**N):
        s = set()
        a = []
        for i in range(N):
            if bit&(1<<i) != 0:
                s.add(P[i]-1)
                s.add(Q[i]-1)
                a.append(i)
    
        if set(range(N)) == s:
            ans += 1
            print(a)

    return ans
