
N,K = map(int,input().split())

P = list(map(int,input().split()))

for i in range(N):
    P[i] = (((1+P[i]))/2)

Q = [0] * (N+1)
for i in range(1,N+1):
    Q[i] = Q[i-1] + P[i-1]

ans = 0
for i in range(N-K+1):
    ans = max(Q[i+K]-Q[i], ans)

print(ans)