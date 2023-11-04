
import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math 



N = int(input())

A = [list(map(int,input().split())) for i in range(N)]

M = int(input())

B = [[[1,0],[0,1],[0,0]]]

for i in range(M):
    
    b = B[-1]
    op = list(map(int,input().split()))
    if op[0] == 2:
        B.append([[-b[1][0],-b[1][1]],[b[0][0],b[0][1]],[-b[2][1],b[2][0]]])
    if op[0] == 1:
        B.append([[b[1][0],b[1][1]],[-b[0][0],-b[0][1]],[b[2][1],-b[2][0]]])
    if op[0] == 3:
        B.append([[-b[0][0],-b[0][1]],[b[1][0],b[1][1]],[-b[2][0]+2*op[1],b[2][1]]])
    if op[0] == 4:
        B.append([[b[0][0],b[0][1]],[-b[1][0],-b[1][1]],[b[2][0],-b[2][1]+2*op[1]]])
    

Q = int(input())

for i in range(Q):
    a,b = map(int,input().split())

    S,T = B[a][:2],B[a][-1]
    x = A[b-1]

    print(S[0][0]*x[0]+S[0][1]*x[1] + T[0], S[1][0]*x[0]+S[1][1]*x[1] + T[1])