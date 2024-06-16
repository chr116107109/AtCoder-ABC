
from copy import deepcopy

H,W = map(int,input().split())
A = [list(map(int,input().split())) for i in range(H)]
B = [[0]*W for i in range(H)]
for i in range(H):
    for j in range(W):
        B[i][j] = 1-A[i][j]
inf = 10**10  
d = [[inf,inf] for i in range(H)]

def isolate(A,B,i):
    res = False
    for j in range(W):
        iso = True
        for t in [-1,1]:
            if 0<=j+t<W:
                if B[i-1][j] == B[i-1][j+t]:
                    iso = False
        if A[i][j] == B[i-1][j]:
            iso = False
        if iso:
            res = True
            break
    
    return res

if not isolate(A,A,1):
    d[0][0] = 0
if not isolate(B,A,1):
    d[0][0] = min(d[0][0],1)
if not isolate(A,B,1):
    d[0][1] = min(d[0][1],1)
if not isolate(B,B,1):
    d[0][1] = min(d[0][1],2)


for i in range(1,H-1):

    if not isolate(A,A,i+1):
        d[i][0] = min(d[i][0],d[i-1][0])
    if not isolate(A,B,i+1):
        d[i][1] = min(d[i][1],d[i-1][0]+1)
    if not isolate(B,A,i+1):
        d[i][0] = min(d[i][0],d[i-1][1])
    if not isolate(B,B,i+1):
        d[i][1] = min(d[i][1],d[i-1][1]+1)