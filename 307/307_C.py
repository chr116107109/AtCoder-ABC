import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

Ha,Wa = map(int,input().split())
A = [input() for i in range(Ha)]
Hb,Wb = map(int,input().split())
B = [input() for i in range(Hb)]
Hx,Wx = map(int,input().split())
X = [list(input()) for i in range(Hx)]
countx = 0
for i in range(Hx):
    for j in range(Wx):
        if X[i][j] == '#':
            countx += 1
ans = 'No'
for i in range(30-Hb):
    for j in range(30-Wb):
        
        C = [['.'] * (30) for _ in range(30)]
        for ii in range(Ha):
            for jj in range(Wa):
                if A[ii][jj] == '#':
                    C[ii+10][jj+10] = '#'
        for ii in range(Hb):
            for jj in range(Wb):
                if B[ii][jj] == '#':
                    C[ii+i][jj+j] = '#'

        count = 0
        for ii in range(30):
            for jj in range(30):
                if C[ii][jj] == '#':
                    count += 1
        
        #for c in C:
        #    print("".join(c))
        #print("")
        if countx != count:
            continue

        #print(*C,sep='\n')
        #print('')
        for h in range(30-Hx):
            for w in range(30-Wx):
                Y = [['.']*(Wx) for _ in range(Hx)]
                for hx in range(Hx):
                    for wx in range(Wx):
                        #print(h+hx,w+wx,C[h+hx][w+wx])
                        if C[h+hx][w+wx] == '#':
                            Y[hx][wx] = '#'
                            #print(Y[hx][wx])
                #print(h,w,Y)
                if Y == X:
                    ans = 'Yes'
                    #print(Y)

                    #print(*Y, sep='\n')
                    #print('')
        
print(ans)
        
