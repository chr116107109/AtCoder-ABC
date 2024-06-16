
N,M = map(int,input().split())
A = list(map(int,input().split()))
D = []
for i in range(N):
    D.append([A[i],1])

for i in range(M):
    B,C = map(int,input().split())
    D.append([C,B])

D.sort(key = lambda x: x[0])

ans = 0
#print(D)
while N>0:
    [B,C] = D.pop()
    if C < N:
        ans += B*C
        N -= C
    else:
        ans += B*N
        break

print(ans)