

N = int(input())
X = [list(map(int,input().split())) for i in range(N)]
Q = int(input())
A = [list(map(int,input().split())) for i in range(Q)]

orix = X[0][0]
oriy = X[0][1]
for i in range(N):
    X[i] = [X[i][0]-orix,X[i][1]-oriy]
for i in range(Q):
    A[i] = [A[i][0]-orix,A[i][1]-oriy]


import math

angle = []
for i in range(1,N):
    x,y = X[i]
    if x == 0:
        if y > 0:
            angle.append(math.pi/2)
        else:
            angle.append(-math.pi/2)
        continue
    angle.append(math.atan(y/x))

import bisect
for i in range(Q):
    x,y = A[i]
    if x == orix:
        if y > 0:
            theta = math.pi/2
        else:
            theta = -math.pi/2
        continue
    theta = math.atan((y-oriy)/(x-orix))

    ind = bisect.bisect_left(angle,theta)

    if ind == 0:
        if y == X[0][0]*x and x < X[0][0]:
            print('ON')
        else:
            print("OUT")
    elif ind == N or ind == N-1:
        if y == X[-1][0]*x and x < X[-1][0]:
            print('ON')
        else:
            print("OUT")
    
