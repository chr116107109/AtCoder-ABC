import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools


N,M,H,K = map(int,input().split())

S = input()

d = set()
for i in range(M):
    x,y = map(int,input().split())
    d.add((x,y))

now = [0,0]
ans = 'Yes'
for i in range(N):
    if H < 0:
        ans = 'No'
        break
    
    if tuple(now) in d and H < K and i > 0:
        d.remove(tuple(now))
        H = K
    
    H -= 1
    if S[i] == 'L':
        now[0] -= 1
    if S[i] == 'R':
        now[0] += 1
    if S[i] == 'U':
        now[1] += 1
    if S[i] == 'D':
        now[1] -= 1
    
if H < 0:
    ans = 'No'
print(ans)