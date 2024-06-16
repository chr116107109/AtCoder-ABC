

R,C = map(int,input().split())
A = [list(input()) for i in range(R)]

import copy
B = copy.deepcopy(A)

for i in range(R):
    for j in range(C):
        if A[i][j] != '#' and A[i][j] != '.':
            n = int(A[i][j])
            
            for l in range(R):
                for k in range(C):
                    if abs(i-l) + abs(k-j) <= n:
                        B[l][k] = '.'

for i in range(R):
    print("".join(B[i]))