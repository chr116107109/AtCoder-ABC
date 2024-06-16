
N,M = map(int,input().split())

visited = [[0]*N for i in range(N)]
import itertools
for i in range(M):
    x = list(map(int,input().split()))
    for y,z in itertools.combinations(x[1:],2):
        visited[y-1][z-1] = 1
        visited[z-1][y-1] = 1

flag = 1
for i in range(N):
    for j in range(N):
        if i == j or visited[i][j] == 1:
            continue
        else:
            flag = 0
            break

if flag == 1:
    print('Yes')
else:
    print('No')

