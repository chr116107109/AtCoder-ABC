
from distutils.spawn import spawn
from posixpath import split


H,W,rs,cs = map(int,input().split())
N = int(input())
walls_H = {}
walls_W = {}
for i in range(N):
    r,c = map(int,input().split())
    if r in walls_H:
        walls_H[r].add(c)
    else:
        walls_H[r] = {c}
    if c in walls_W:
        walls_W[c].add(r)
    else:
        walls_W[c] = {r}
    
for wal in walls_H:
    walls_H[wal] = sorted(list(walls_H[wal]))
for wal in walls_W:
    walls_W[wal] = sorted(list(walls_W[wal]))

import bisect

Q = int(input())
for i in range(Q):
    d,l = input().split()
    l = int(l)
    if d == 'L':
        if rs in walls_H:
            ind = bisect.bisect_left(walls_H[rs],cs)
            if ind == 0:
                buffer = cs - 1
            else:
                buffer = cs - (walls_H[rs][ind-1] + 1)
        else:
            buffer = cs - 1
        #print(d,buffer,ind)
        cs -= min(buffer,l)
    if d == 'R':
        if rs in walls_H:
            ind = bisect.bisect_left(walls_H[rs],cs)
            if ind == len(walls_H[rs]):
                buffer = W - cs
            else:
                buffer = (walls_H[rs][ind] - 1)  - cs
        else:
            buffer = W - cs
        #print(buffer)
        cs += min(l,buffer)
    if d == 'U':
        if cs in walls_W:
            ind = bisect.bisect_left(walls_W[cs],rs)
            if ind == 0:
                buffer = rs - 1
            else:
                buffer = rs - (walls_W[cs][ind-1] + 1)
        else:
            buffer = rs - 1
        #print(ind,buffer)
        rs -= min(buffer,l)
    if d == 'D':
        if cs in walls_W:
            ind = bisect.bisect_left(walls_W[cs],rs)
            if ind == len(walls_W[cs]):
                buffer = H-rs
            else:
                buffer = (walls_W[cs][ind] - 1) - rs
        else:
            buffer = H-rs
        rs += min(l,buffer)
    print(rs,cs)