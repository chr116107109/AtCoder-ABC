

N,X = map(int,input().split())
A = [list(map(int,input().split())) for i in range(N)] 

q = []
for i in range(A[0][0]):
    q.append([A[0][i+1], 0])
ans = 0
while q:
    #print(q)
    [v,i] = q.pop()
    if i < N-1:
        for j in range(A[i+1][0]):
            q.append([v*A[i+1][j+1],i+1])
    elif v == X:
        ans += 1
        
print(ans)