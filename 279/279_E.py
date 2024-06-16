
N,M = map(int,input().split())
A = list(map(int,input().split()))
B = list(range(N+1))
C = list(range(N+1))

for i in range(M-1,0,-1):
    C[A[i]],C[A[i]+1] = C[A[i]+1],C[A[i]]

now = 1
for i in range(M):
    print(C[now])
    #print(C)
    if A[i] == now:
        now += 1
    elif A[i] == now-1:
        now -= 1
    
    if i+1 > M-1:
        continue
    C[A[i+1]],C[A[i+1]+1] = C[A[i+1]+1],C[A[i+1]]