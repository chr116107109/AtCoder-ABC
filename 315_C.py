import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math


H,W = map(int,input().split())
A = [list(input()) for i in range(H)]

tate = [{} for i in range(W)]
yoko = [{} for i in range(H)]


c2p = {}
for i in range(H):
    for j in range(W):
        if A[i][j] in tate[j]:
            tate[j][A[i][j]] += 1
        else:
            tate[j][A[i][j]] = 1
        if A[i][j] in yoko[i]:
            yoko[i][A[i][j]] += 1
        else:
            yoko[i][A[i][j]] = 1



count = H*W
h,w = H,W
X = set(range(W))
Y = set(range(H))
while A:
    #print(tate)
    #sprint(yoko)
    #print(count)
    y_vanish = []
    for i in Y:
        if len(yoko[i]) == 1 and w > 1:
            y_vanish.append([i,list(yoko[i].keys())[0]])
    
    x_vanish = []
    for j in X:
        if len(tate[j]) == 1 and h > 1:
            x_vanish.append([j,list(tate[j].keys())[0]])

    #print(x_vanish)
    #print(y_vanish)

    if x_vanish == [] and y_vanish == []:
        break

    p_vanish = set()
    for y,c in y_vanish:
        for x in X:
            if c in tate[x]:
                tate[x][c] -= 1
                if tate[x][c] == 0:
                    del tate[x][c]

                #p_vanish.add((c,p))
        
    for x,c in x_vanish:
        for y in Y:
            if c in yoko[y]:
                yoko[y][c] -= 1
                if yoko[y][c] == 0:
                    del yoko[y][c]
                
                #p_vanish.add((c,p))


    for x,_ in x_vanish:
        X.remove(x)
        tate[x] = {}
    for y,_ in y_vanish:
        Y.remove(y)
        yoko[y] = {}

    count -= len(y_vanish)*w + len(x_vanish)*h - len(y_vanish)*len(x_vanish)
    h -= len(y_vanish)
    w -= len(x_vanish)

print(len(X)*len(Y))
