
N = int(input())

TKA = [list(map(int,input().split())) for i in range(N)]

T = [TKA[i][0] for i in range(N)]
K = [TKA[i][1] for i in range(N)]
A = [TKA[i][2:] for i in range(N)]

q = []
q.append(N-1)
visited = set()
ans = 0
while q:
    s = q.pop()
    if s in visited:
        continue
    visited.add(s)
    ans += T[s]
    for t in A[s]:
        q.append(t-1)

print(ans)