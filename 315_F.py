
import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

N = int(input())
A = [list(map(int,input().split())) for i in range(N)]

M = 50
inf = 10**10
d = [[inf] * M for i in range(N)]

d[0][0] = 0

def f(a,b):
    return math.sqrt((a[0]-b[0])**2+(a[1]-b[1])**2)

d[1][0] = f(A[0],A[1])

for i in range(2,N):
    for j in range(1,M):
        for k in range(M):
            if M > j+k-1 >= 0 and i-j >= 0 :
                d[i][j+k-1] = min(d[i][j+k-1], d[i-j][k] + f(A[i-j], A[i]))
                #print(j+k-1,k,d[i-j][k])
        #print(d[i])
ans = d[-1][0]
for i in range(1,M):
    ans = min(ans, d[-1][i]+pow(2,i-1))

print(ans)