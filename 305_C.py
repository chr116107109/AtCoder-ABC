import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

H,W = map(int,input().split())
S = [input() for i in range(H)]

for i in range(H):
    for j in range(W):
        if S[i][j] == '#':
            continue
        count = 0
        for a,b in [(i,j+1),(i+1,j),(i,j-1),(i-1,j)]:
            if 0<=a<H and 0<=b<W:
                if S[a][b] == '#':
                    count += 1

        if count >= 2:
            print(i+1,j+1)
            break
