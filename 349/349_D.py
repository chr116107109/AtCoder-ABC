import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math



L,R = map(int,input().split())


q = []
visited = {}
q.append([L,R])
ans = []
while q:
    l,r = q.pop()
    #print(l,r)
    if (l,r) in visited:
        continue

    if r - l == 1:
        ans.append([l,r])
        visited[(l,r)] = 1
        continue
    visited[(l,r)] = 1

    for x in range(61,-1,-1):
        if r - l >= pow(2,x):

            j = r//pow(2,x) - 1
            if l <= j * pow(2,x) and (j+1) * pow(2,x) <= r:
                pass
            else:
                continue
            
            ans.append([j * pow(2,x), (j+1) * pow(2,x)])

            if j * pow(2,x) != l:
                q.append([l,j * pow(2,x)])
            if (j+1) * pow(2,x) != r:
                q.append([(j+1) * pow(2,x),r])
            break


ans.sort(key=lambda x: x[0] )
print(len(ans))
for a in ans:
    print(a[0],a[1])