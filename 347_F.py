import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

N,M = map(int,input().split())

A = [list(map(int,input().split())) for _ in range(N)]

# 2次元累積和
B = [[0]*(N+1) for _ in range(N+1)]

for i in range(N):
    for j in range(N):
        B[i+1][j+1] = B[i+1][j] + B[i][j+1] - B[i][j] + A[i][j]

q = []

for i in range(N-M+1):
    for j in range(N-M+1):
        score = B[i+M][j+M] - B[i][j+M] - B[i+M][j] + B[i][j]
        heappush(q,(-score,i,j))

ans = []
#print(q)
def is_intersect(ans,i,j):
    for a in ans:
        if max(i,a[1]) < min(i+M,a[1]+M) and max(j,a[2]) < min(j+M,a[2]+M):
            return True
    return False
    
while len(ans) < 3 and q:
    score,i,j = heappop(q)
    if not is_intersect(ans,i,j):
        ans.append((-score,i,j))

print(sum([x[0] for x in ans]))