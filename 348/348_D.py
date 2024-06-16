import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

H,W = map(int,input().split())

A = [list(input()) for _ in range(H)]

for i in range(H):
    for j in range(W):
        if A[i][j] == 'S':
            start = (i,j)
        if A[i][j] == 'T':
            goal = (i,j)

N = int(input())

B = [list(map(int,input().split())) for _ in range(N)]

def f(x,y):
    return x*W+y

B_set = [[0] * W for _ in range(H)]
for i in range(N):
    B_set[B[i][0]-1][B[i][1]-1] = B[i][2]

def bfs(start,goal):
    q = deque()
    q.append((start,0))
    energy = [[0] * W for _ in range(H)]

    while q:
        (x,y),e = q.popleft()
        #print(x,y,e)
        #print(energy)
        e = max(e,B_set[x][y])
        if (x,y) == goal:
            return True
        if e <= energy[x][y]:
            continue
        energy[x][y] = e
        if e == 0:
            continue

        for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            nx = x + dx
            ny = y + dy

            if 0 <= nx < H and 0 <= ny < W:
                if A[nx][ny] == '#':
                    continue
                else:
                    q.append(((nx,ny),e-1))

    return False

if bfs(start,goal):
    print('Yes')
else:
    print('No')