
import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math
import sys

def f(x,y):
    return ((x[0]-y[0])**2 + (x[1]-y[1])**2)


N = int(input())

A = [list(map(int,input().split())) for i in range(N)]

l = 0
r = 1010

far_dist = [0] * N
for i in range(N):
    for j in range(N):
        far_dist[i] = max(far_dist[i],f(A[i],A[j]))


eps = 10**(-10)
while abs(l-r) > eps:
    m = (l+r)/2
    #print(m)
    points = set()
    for i in range(N):
        for j in range(i+1,N):
            if f(A[i],A[j]) > (2*m)**2:
                continue
            x1,y1 = A[i]
            x2,y2 = A[j]
            a = 2*(x1-x2)
            b = 2*(y1-y2)
            c = x2**2 - x1**2 + y2**2 - y1**2

            D = abs(a*x2 + b*y2 + c)

            Ax = (a*D - b*math.sqrt((a**2+b**2)*m**2 - D**2))/(a**2+b**2) + x2
            Ay = (b*D + a*math.sqrt((a**2+b**2)*m**2 - D**2))/(a**2+b**2) + y2

            Bx = (a*D + b*math.sqrt((a**2+b**2)*m**2 - D**2))/(a**2+b**2) + x2
            By = (b*D - a*math.sqrt((a**2+b**2)*m**2 - D**2))/(a**2+b**2) + y2

            points.add((Ax,Ay))
            points.add((Bx,By))
    #print(points)

    ok = False
    for x,y in points:
        _in = True
        for i in range(N):
            if f(A[i],[x,y]) > m**2 + eps:
                _in = False
                break
        if _in:
            ok = True
            break

    if ok :
        r = m
    else:
        l = m

print(l)