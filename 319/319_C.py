import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math


A = [list(map(int,input().split())) for i in range(3)]


def check(p):
    ok = True
    tate = [Counter(),Counter(),Counter()]
    yoko =  [Counter(),Counter(),Counter()]
    naname = [Counter(),Counter()]

    for i in p:
        x,y = i//3,i%3
        tate[x][A[x][y]] += 1
        if tate[x][A[x][y]] == 2 and len(tate[x].keys()) == 1:
            ok = False
            break
        yoko[y][A[x][y]] += 1
        if yoko[y][A[x][y]] == 2 and len(yoko[y].keys()) == 1:
            ok = False
            break        
        if x == y:
            naname[0][A[x][y]] += 1
            if naname[0][A[x][y]] == 2 and len(naname[0].keys()) == 1:
                ok = False
                break
            
        if x + y == 2:
            naname[-1][A[x][y]] += 1
            if naname[-1][A[x][y]] == 2 and len(naname[-1].keys()) == 1:
                ok = False
                break
    return ok,tate,yoko,naname

count = 0
for p in itertools.permutations(range(9)):
    ok, tate, yoko, naname = check(p)
    if ok:
        count += 1
        #print(p)
        

print(count/math.perm(9))