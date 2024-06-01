import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math


N,T = map(int,input().split())

A = list(map(int,input().split()))

bingo = [[0]*N for _ in range(N)]

tate_count = [0]*N
yoko_count = [0]*N
naname_count_1 = 0
naname_count_2 = 0

for i in range(T):
    a = A[i] - 1

    tate = a//N
    yoko = a%N

    bingo[tate][yoko] = 1

    tate_count[tate] += 1
    yoko_count[yoko] += 1

    if tate == yoko:
        naname_count_1 += 1
    if tate == N-1-yoko:
        naname_count_2 += 1

    if tate_count[tate] == N or yoko_count[yoko] == N or naname_count_1 == N or naname_count_2 == N:
        print(i+1)
        sys.exit()

print(-1)