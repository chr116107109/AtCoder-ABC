
N,K = map(int,input().split())
RSP = list(map(int,input().split()))
A = list(input())

ans = [0] * N
rsp = 'rsp'

for i in range(K):
    ans[i] = ans[i-1]
    for j in range(3):
        if A[i] == rsp[(j+1)%3]:
            ans[i] += RSP[j]

for i in range(K,N):
    ans[i] = ans[i-1]
    for j in range(3):
        if A[i] == rsp[(j+1)%3]:
            if A[i-K] == A[i]:
                A[i] = 'n'
                continue
            ans[i] += RSP[j]

print(ans[-1])