
N = int(input())
A = list(map(int,input().split()))

B = [0]
for i in range(N):
    B.append(B[-1]+A[i])

C = [0]
for i in range(1,N+1):
    C.append(C[-1]+B[i])


D = 0
ans = 0

for i in range(1,N):
    D = max(D,B[i-1])
    ans = max(ans,C[i]+D)

ans = max(C[-1],ans)
print(ans)