
import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

N,C = map(int,input().split())
A = [list(map(int,input().split())) for i in range(N)]

l = deque()
l.append([0,0])
l_score = 0
r = deque()
r.append([0,0])
r_score = 0
s = 0
x = 0
for i in range(N):
    s += A[i][1]
    s -= A[i][0]
    if r_score < s:
        r_score = s
        x = A[i][0]
    r.append([x,r_score])
    s += A[i][0]
l_score = 0


ans = r_score
s = 0
y = 0
r.pop()
for i in range(N):
    x,r_score = r.pop()
    
    
    s += A[-i-1][1]
    s -= C - A[-i-1][0]
    if l_score < s:
        y,l_score = C-A[-i-1][0], s
    l.append([y,l_score])
    #print(s)
    s += C - A[-i-1][0]
    
    #print(l,l_score)
    #print(r,r_score)
    
    
    ans = max(ans, -min(x,y) + r_score + l_score)

print(ans)