
import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

N,M = map(int,input().split())
A = list(map(int,input().split()))

'''
oooxxoxoxxoxxo
のoxの個数を数えると考えられる
'''

inf = 10**10

before = [[inf,inf] for i in range(M+1)]
after = [[inf,inf] for i in range(M+1)]
before[0][0] = 0
before[0][1] = 1

for i in range(N):
    for j in range(M+1):
        after[j][1] = min(after[j][1], before[j][1]) # x -> x
        after[j][1] = min(after[j][1], before[j][0]+1) # o-> x    
        if j+A[i] <= M:
            after[j+A[i]][0] = min(after[j+A[i]][0], before[j][0]) # o -> o
            after[j+A[i]][0] = min(after[j+A[i]][0], before[j][1]) # x -> o

    before = after[:]
    after = [[inf,inf] for i in range(M+1)]

for i in range(1,M+1):
    if min(before[i]) == inf:
        print(-1)
    else:
        print(min(before[i]))