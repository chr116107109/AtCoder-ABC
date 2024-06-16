
import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

N = int(input())

d = [[-1]*13 for i in range(N)]
f = [[-1]*13 for i in range(N)]
count = 1
interval = []
for i in range(N):
    #print(i+1,i+1,flush=True)
    interval.append([i+1,i+1])
    d[i][0] = count
    f[i][0] = count
    count += 1
    for j in range(13):
        if i+2**j >= N:
            break
        d[i+2**j][j+1] = count
        f[i][j+1] = count
        #print(i+1,i+2**j+1,flush=True)
        interval.append([i+1,i+2**j+1])
        count += 1

print(len(interval))
for l,r in interval:
    print(l,r)

Q = int(input())
for i in range(Q):
    l,r = map(int,input().split())
    l -= 1
    r -= 1
    if l == r:
        print(d[l][0],d[l][0],flush=True)
    else:
        ans = [-1,-1]
        for j in range(13):
            if l+2**j > r:
                ans[0] = f[l][j]
                break
        ans[1] = d[r][j]
        print(*ans,flush=True)
        #print(interval[ans[0]-1],interval[ans[1]-1])