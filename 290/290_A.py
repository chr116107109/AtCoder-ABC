
N,M = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

ans = 0
for i in range(M):
    ans += A[B[i]-1]

print(ans)