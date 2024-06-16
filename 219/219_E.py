

import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

A = [list(map(int,input().split())) for i in range(4)]
house_count = 0

edge = {(0,0),(1,0),(2,0),(3,0),(0,1),(0,2),(0,3),(1,3),(2,3),(3,3),(3,1),(3,2)}
for i in range(4):
    for j in range(4):
        if A[i][j] == 1:
            house_count += 1

ans = 0
for bit in range(1,2**16):
    d = [[0]*4 for i in range(4)]
    
    count = 0
    for i in range(4):
        for j in range(4):
            if bit&(1<<i*4+j) != 0:
                count += 1
                d[i][j] = 1
                start = (i,j)

    cross = False
    inzero = []
    for i in range(1,3):
        for j in range(1,3):
            if d[i][j] == 0:
                inzero.append((i,j))
                wamari_count = 0
                for l,r in [(i,j+1),(i+1,j),(i,j-1),(i-1,j)]:
                    if 0<=l<4 and 0<=r<4 and d[l][r] == 1:
                        wamari_count += 1
                if wamari_count == 4:
                    cross = True
    visited = set()
    for i,j in inzero:
        if (i,j) in visited:
            continue
        q = deque()
        q.append((i,j))   
        ok = False     
        while q:
            s = q.popleft()
            if s in visited:
                continue
            if s in edge:
                ok = True
            visited.add(s)
            i,j = s
            for l,r in [(i,j+1),(i+1,j),(i,j-1),(i-1,j)]:
                if 0<=l<4 and 0<=r<4 and d[l][r] == 0:
                    q.append((l,r))
        
        if not ok :
            cross = True
        
    q = deque()
    q.append(start)
    visited = set()
    inside_count = 0
    while q:
        s = q.popleft()
        if s in visited:
            continue
        visited.add(s)
        i,j = s
        if A[i][j] == 1:
            inside_count += 1
        for l,r in [(i,j+1),(i+1,j),(i,j-1),(i-1,j)]:
            if 0<=l<4 and 0<=r<4 and d[l][r] == 1:
                q.append((l,r))
    
    if len(visited) == count and inside_count == house_count and not cross:
        #print(d)
        ans += 1


print(ans)