
N,M,Q = map(int,input().split())
A = [list(map(int,input().split())) for i in range(Q)]

q = []
for i in range(M):
    q.append([i+1])
S = []
while q:
    li = q.pop()
    if len(li) == N:
        S.append(li)
        continue
    now = li[-1]
    for next in range(now,M+1):
        q.append(li+[next])

ans = 0
for li in S:
    sub = 0
    for k in range(Q):
        [a,b,c,d] = A[k]
        if li[b-1]-li[a-1] == c:
            sub += d
    ans = max(ans,sub)

print(ans)