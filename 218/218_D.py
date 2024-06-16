import math
from itertools import combinations
N = int(input())
C_X = {}
C_Y = {}
for i in range(N):
    x,y = map(int,input().split())
    if x in C_X:
        C_X[x].add(y)
    else:
        C_X[x] = {y}
    

ans = 0
for i,j in combinations(C_X,2):
    c = len(C_X[i]&C_X[j])
    if c > 1:
        ans += c*(c-1)//2

print(ans)