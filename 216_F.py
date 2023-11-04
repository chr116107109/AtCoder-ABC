
N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

C = [[A[i],B[i]] for i in range(N)]
C.sort(key=lambda x:x[0])
M = 5001#max(A)
d = [[0]*(M+1) for i in range(N)]

#d[0][A[0]] += 1
mod = 998244353
ans = 0
d[0][0] = 1
d[0][C[0][1]] = 1
if C[0][0] >= C[0][1]:
    ans += 1
for i in range(1,N):
    a,b = C[i]
    #d[i][0] = 1
    for j in range(M+1):
            
        if d[i-1][j] > 0 and j+b <= M:
            d[i][j+b] += d[i-1][j]
            d[i][j+b] %= mod
    for j in range(1,a+1): 
        ans += d[i][j]
        ans %= mod

    for j in range(M+1):
        d[i][j] += d[i-1][j]
        d[i][j] %= mod
    #print(ans)
print(ans)