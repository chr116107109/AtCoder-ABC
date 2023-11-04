import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

N,M = map(int,input().split())

H = list(map(int,input().split()))
W = list(map(int,input().split()))

H.sort()
W.sort()

l = [0]
for i in range(N//2):
    l.append(l[-1] + abs(H[2*i] - H[2*i+1]))
r = [0]
for i in range(N//2):
    r.append(r[-1] + abs(H[N-1-2*i] - H[N-2-2*i]))


ans = 10**20
for i in range(N):
    ind = bisect_left(W,H[i])
    s = min(abs(W[ind]-H[i]),abs(W[min(ind+1,M-1)] - H[i]))
    if i%2 == 0:
        ans = min(ans, s + l[i*2] + r[N-i*2-1])
    else:
        ans = min(ans, s + l[i*2] + r[N-i*2-1])