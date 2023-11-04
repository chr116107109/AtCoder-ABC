

N,M = map(int,input().split())
B = []
for i in range(M):
    a,b = map(int,input().split())
    B.append([a-1,b-1])

K = int(input())
A = [list(map(int,input().split())) for i in range(K)]

ans = 0
for i in range(2**K):
    score = 0
    boll = [0]*N
    for j in range(K):
        if i&(1<<j) != 0:
            boll[A[j][0]-1] = 1
        else:
            boll[A[j][1]-1] = 1
    
    for j in range(M):
        if boll[B[j][0]] == boll[B[j][1]] == 1:
            score += 1
    
    ans = max(ans,score)

print(ans)