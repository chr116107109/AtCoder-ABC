
N,M = map(int,input().split())
A = []
for i in range(M):
    C = int(input())
    A.append(set(map(int,input().split())))

ans = 0

for i in range(2**M):
    S = set()
    for j in range(M):
        if i & (1<<j) != 0:
            S = S|A[j]

    ok = True
    for x in range(1,N+1):
        if not x in S:
            ok = False
            break
    
    if ok:
        ans += 1
print(ans)  