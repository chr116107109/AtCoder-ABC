
import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

A = [list(input()) for i in range(4)]
B = [list(input()) for i in range(4)]
C = [list(input()) for i in range(4)]

def left_up(X): 
    lu = []
    Y = []
    for i in range(4):
        if "#" in X[i]:
            Y.append(X[i])
def rot90(A):
    return list(zip(*(A[::-1])))


ans = "No"
for i in range(16):
    for j in range(16):
        for k in range(16):

            for a in range(4):
                A = rot90(A)
                for b in range(4):
                    B = rot90(B)
                    for c in range(4):
                        C = rot90(C)
                        
                        X = [['.']*4 for i in range(4)]
                        ok = True
                        for xx in range(4):
                            for yy in range(4):
                                X[i//8+xx][i%8+yy] = A[xx][yy]
                        for xx in range(4):
                            for yy in range(4):
                                if X[j//8+xx][j%8+yy] == B[xx][yy] == '#':
                                    ok = False
                                X[j//8+xx][j%8+yy] = B[xx][yy]
                        for xx in range(4):
                            for yy in range(4):
                                if X[k//8+xx][k%8+yy] == C[xx][yy] == '#':
                                    ok = False
                                X[k//8+xx][k%8+yy] = B[xx][yy]
                        
                        for x in range(4):
                            for y in range(4):
                                if (not (4 <= x < 8 and 4<=y<8)) and X[x][y] == '#':
                                    ok = False
                        
                        print(*X,sep='\n')
                        print('')
                        if ok:
                            ans = "Yes"

print(ans)