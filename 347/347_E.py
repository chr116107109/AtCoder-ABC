import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

N,Q = map(int,input().split())
X = list(map(int,input().split()))

point = [0]*N
enter_time = [-1]*N
group_point = [0]

S = set()
for i in range(Q):
    if X[i]-1 in S:
        S.remove(X[i]-1)
        enter = enter_time[X[i]-1]
        p = group_point[-1]-group_point[enter]
        point[X[i]-1] += p
        group_point.append(group_point[-1]+len(S))

    else:
        S.add(X[i]-1)
        group_point.append(group_point[-1]+len(S))
        enter_time[X[i]-1] = i

    #print(point)
    #print(group_point)
    #print(enter_time)
    #print(S)

for i in S:
    enter = enter_time[i]
    p = group_point[-1]-group_point[enter]
    point[i] += p
print(*point)