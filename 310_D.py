
import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

N,T,M = map(int,input().split())

g = [set() for i in range(N)]
for i in range(M):
    a,b = map(int,input().split())
    g[a-1].add(b-1)
    g[b-1].add(a-1)


ans = set()

for s in itertools.combinations(range(N),T):
    a = []
    b = []
    for i in range(N):
        if i in s:
            a.append(i)  
        else:
            b.append(i)
    a.sort()
    b.sort()
    for bit in range(T**(N-T)):
        d = [[ss] for ss in a]
        ok = True
        for i in range(N-T-1,-1,-1):
            j = bit//(T**i)
            bit %= (T**i)
            if d[j][-1] < b[i]:
                ok = False
                break
            d[j].append(b[i])
        if not ok:
            continue
        for i in range(T):
            d[i].sort()

        ok = True
        for i in range(T):
            for j in d[i]:
                for k in g[j]:
                    if k in d[i]:
                        ok = False
                    if not ok:
                        break
                if not ok:
                    break
            if not ok:
                break
            
        if ok:
            d.sort()
            ans.add(str(d))


print(len(ans))