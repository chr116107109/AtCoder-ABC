import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

N,M = map(int,input().split())


S = [input() for i in range(N)]

for i in range(N-8):
    for j in range(M-8):
        
        ok = True
        for x in range(9):
            for y in range(9):
                if x<= 2 and y <= 2 and S[i+x][j+y] != '#':
                    ok = False
                if x>= 6 and y >= 6 and S[i+x][j+y] != '#':
                    ok = False
        for x in range(4):
            if S[i+3][j+x] != '.':
                ok = False
        for x in range(4):
            if S[i+x][j+3] != '.':
                ok = False
        for x in range(4):
            if S[i+5][j+5+x] != '.':
                ok = False
        for x in range(4):
            if S[i+5+x][j+5] != '.':
                ok = False
        
        if ok:
            print(i+1,j+1)

        
        