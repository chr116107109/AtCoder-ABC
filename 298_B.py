

N = int(input())
A = [list(map(int,input().split())) for i in range(N)]
B = [list(map(int,input().split())) for i in range(N)]

import copy
C = copy.deepcopy(A)

for _ in range(8):
    for i in range(N):
        for j in range(N):

            C[i][j] = A[N-1-j][i]
    
    ans = 'Yes'
    for i in range(N):
        for j in range(N):
            if C[i][j] == 1:
                if B[i][j] != 1:
                    ans = 'No'
    if ans == 'Yes':
        break 
    A = copy.deepcopy(C)

print(ans)
