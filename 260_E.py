
import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

N,M = map(int,input().split())
A = [list(map(int,input().split())) for i in range(N)]

ans = [0] * (M+1)

edge = max([a[0] for a in A])
last = min([a[1] for a in A])
#ans[edge] += 1
q = []
d = Counter()
for i in range(N):
    q.append([A[i][0],i])
    q.append([A[i][1],i])

    d[A[i][0]] = max(d[A[i][0]], A[i][1])

for i in range(1,last+1):
    ans[edge-i] += 1
    ans[M-i+1] -= 1
    if i in d:
        edge = max(edge,d[i])

    #print(ans)

#print(ans)
for i in range(M):
    ans[i+1] += ans[i]  

ans.pop()
print(*ans)