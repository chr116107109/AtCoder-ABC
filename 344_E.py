import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

N = int(input())
A = list(map(int,input().split()))

aset = set(A)
parent = {}
child = {}
child[-1] = A[0]
parent[A[0]] = -1
for i in range(1,N):
    parent[A[i]] = A[i-1]
    child[A[i-1]] = A[i]
child[A[N-1]] = -10
parent[-10] = A[N-1]
Q = int(input())

ans = []
for i in range(Q):
    q = list(map(int,input().split()))

    if q[0] == 1:
        x,y = q[1],q[2]
        c = child[x]

        parent[c] = y
        child[y] = c

        parent[y] = x
        child[x] = y

    elif q[0] == 2:
        x = q[1]

        p = parent[x]
        c = child[x]
        child[p] = c
        parent[c] = p

now = -1
while True:
    if child[now] == -10:
        break   
    now = child[now]
    ans.append(now)

print(*ans) 