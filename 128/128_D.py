
N,K = map(int,input().split())

V = list(map(int,input().split()))
ans = 0

for l in range(N+1):
    for r in range(N+1):
        if l+r > N or l+r > K:
            continue
        
        A = []
        for i in range(l):
            A.append(V[i])
        for i in range(r):
            A.append(V[N-1-i])
        A.sort()
        score = sum(A)
        for i in range(min(l+r, K - l-r)):
            if A[i] > 0:
                break
            score -= A[i]
        ans = max(ans,score)

print(ans)