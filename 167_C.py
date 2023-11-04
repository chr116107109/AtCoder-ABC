
N,M,X = map(int,input().split())
C = []
A = []
for i in range(N):
    inp = list(map(int,input().split()))
    C.append(inp[0])
    A.append(inp[1:])

ans = 10**20
for i in range(2**N):
    score = [0] * M 
    cost = 0
    for j in range(N):
        if i & (1<<j) != 0:
            for k in range(M):
                score[k] += A[j][k]
            cost += C[j]
    
    flag = True
    for k in range(M):
        if score[k] < X:
            flag = False
            break
    
    if flag:
        ans = min(ans,cost)

if ans == 10**20:
    print(-1)
else:
    print(ans)